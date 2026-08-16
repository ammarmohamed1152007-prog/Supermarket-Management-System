```mermaid
flowchart TD
    A[Start] --> B[Login Menu]
    B -->|1. Admin| C[Admin Menu]
    B -->|2. Employee| D[Employee Menu]
    B -->|3. Customer| E[Customer Menu]
    B -->|4. Exit| Z[End]

    %% Admin flow
    C --> C1[Add Product]
    C --> C2[List Products]
    C --> C3[Remove Product]
    C --> C4[Hire Employee]
    C --> B

    %% Employee flow
    D --> D1[List Products]
    D --> D2[Process Orders]
    D --> B

    %% Customer flow
    E --> E1[List Products]
    E --> E2[Add to Cart]
    E --> E3[Checkout]
    E -->|Checkout| F[Create Order]
    F --> G[Process Order by Employee]
    G --> H[Make Payment]
    H --> I[Generate Receipt]
    I --> B
    E --> E4[Cancel Shopping] --> B
