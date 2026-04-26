```mermaid
sequenceDiagram
    participant C as Boundary@{ "type" : "boundary" }
    participant S as Service
    C->>S: Request from boundary
    S->>C: Response to boundary
```
