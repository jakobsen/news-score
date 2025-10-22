[parallel]
serve: serve-backend serve-frontend

[working-directory: 'backend']
serve-backend:
    uv run litestar run

[working-directory: 'frontend']
serve-frontend:
    pnpm dev
