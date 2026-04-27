```mermaidflowchart TD
    START([START])
    END([END])

    chatbot["chatbot - calls LLM with state"]
    tools["tools - executes tool calls"]
    route{{"route_tools - tools called?"}}

    START --> chatbot
    chatbot --> route
    route -- "yes: has tool_calls" --> tools
    route -- "no: plain response" --> END
    tools --> chatbot```
