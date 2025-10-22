import "./App.css";
import { Button } from "./components/Button";
import { Input } from "./components/Input";

function App() {
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
  };

  return (
    <main>
      <h1>NEWS score calculator</h1>
      <form onSubmit={handleSubmit}>
        <Input
          id="body-temp"
          label="Body temperature"
          subLabel="Degrees celcius"
        />
        <Input id="heart-rate" label="Heartrate" subLabel="Beats per minute" />
        <Input
          id="respiratory-rate"
          label="Respiratory rate"
          subLabel="Breaths per minute"
        />
        <div className="actions">
          <Button>Calculate NEWS score</Button>
          <Button type="reset" variant="secondary">
            Reset form
          </Button>
        </div>
      </form>
    </main>
  );
}

export default App;
