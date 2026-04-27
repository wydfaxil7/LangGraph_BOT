```mermaid
flowchart TD
    START([START])
    END([END])

    chatbot["chatbot - calls LLM"]
    tools["tools - runs tool calls"]
    route{"tools called?"}

    START --> chatbot
    chatbot --> route
    route -- yes --> tools
    route -- no --> END
    tools --> chatbot
` ``
```
