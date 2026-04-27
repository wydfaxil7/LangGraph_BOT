```mermaid
flowchart TD
    START(([START]))
    END(([END]))

    chatbot["chatbot\ncalls LLM with state"]
    tools["tools\nexecutes tool calls"]
    route{{"route_tools()\ntools called?"}}

    START --> chatbot
    chatbot --> route
    route -- "yes: has tool_calls" --> tools
    route -- "no: plain response" --> END
    tools --> chatbot
```
