# NEWS score calculator

This is a micro web application that implements a simplified version of the NEWS
heuristic calculation. The frontend is written in Typescript and uses
[React](https://react.dev/), whilst the backend is a Python application using
the [Litestar web framework](https://litestar.dev/).

To run the project, you will need to have both [`pnpm`](https://pnpm.io/) and
[`uv`](https://docs.astral.sh/uv/) installed. If you also have
[`just`](https://github.com/casey/just), you can run the project with
```sh
just serve
```
This will run the frontend on `localhost:5173` and the backend on
`localhost:8000`. Alternatively, the frontend and the backend may be started
separately:
```sh
cd frontend
pnpm dev

# And in another terminal:
cd backend
uv run litestar run
```

The backend has a few tests. These can be run with
```sh
cd backend
uv run pytest
```


## Design choices

### Backend

To ensure correctness in the backend, the domain is modelled with `Pydantic` on
the backend.
Using [constrained
types](https://docs.pydantic.dev/2.3/usage/types/number_types/#constrained-types)
allows us to handle invalid input at the border of our program and return
a validation error if we received incomplete or invalid measurements.
This makes the core logic of the program simpler, as we know that we can
trust the data that makes it to our functions. This approach is inspired
by the great 2019 article [Parse, don't validate by Alexis
King](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/).

Even though Python is a dynamic language which ignores the type hints at
runtime, the type hints are used at runtime by litestar and are also used
to generate the OpenAPI schema.

### Frontend

The frontend is deliberately kept very simple. Except for React, Typescript,
vite and their build dependencies, only two additional dependencies are used:

- `@fontsource-variable/inter`, for self-hosting a web-optimized version of
  of the Inter font.
- `zod`, for parsing the API response from our backend into a well-formed
  typescript object.

Notably, the styling is all vanilla CSS. In bigger projects with more components
I would most likey prefer to use a library which makes encapsulation easier,
such as [CSS Modules](https://github.com/css-modules/css-modules),
[DaisyUI](https://daisyui.com/) or [Tailwind CSS](https://tailwindcss.com/).

I also opted to use the browser's native `fetch` to communicate with the backend.
If this were a bigger project the module would either have to be expanded, or
it could benefit from using a data fetching library with better built-in support
for response parsing as well as loading and error states.

## What's missing?

Plenty of things!

On the backend side of things, the testing is quite sparse and would benefit
from an expansion: Edge cases, verification of error messages, etc.

On the frontend, the current amount of error handling is zero, which obviously
wouldn't fly in a real-world scenario. Two obvioius improvements are immediately
clear:
- Have some client-side validation of the form input before sending requests to the backend
- Handle errors from the backend and display a suitable and helpful error message

I opted not to focus on these issues here. Even though there is a lot of prior
art on the UX of good form and inputs, getting them to feel right and be
accessible for everyone can take a surprising amount of time.

On the topic of client-side validation, I also believe that the best application
clients are as thin as possible. That is, they should ideally contain as little
business logic as possible, and instead function as a pure presentational layer.
In this case, it would mean that to draw the form, the frontend would first make
a request to the backend to fetch the schema, including field names and
constraints, and then use this information to render a form with the proper
validation rules. However, implementing this as a part of this project would
have been out of scope.

Finally for the frontend, it feels very bland and dead as-is. There are no hover states,
the score card suddenly appears without any fade-in or similar. This can feel very
jarring and is something I'd like to address in a proper application.

For the project as a whole, it could also benefit from a CI pipeline which checked linting,
formatting and ran the test suite for each commit, and if everything is green, a CD pipeline
to production.
