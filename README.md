git clone <link> 

install google-adk 

After that go to Agents/sub_agents in CLI 

and run adk web  in Administrator command prompot



graph TD
    A[Start: Designer works in Figma] --> B{Needs Design Feedback?};
    B -- Yes --> C[Opens Heurica/Lovable.dev Plugin];
    C --> D(Verify Logged In);
    D --> E[Selects Figma Frame(s)];
    E --> F[Clicks 'Run Audit'];
    F --> G((System: Plugin sends data to Backend));
    G --> H((System: Backend analyzes Heuristics & Copy));
    H --> I((System: Backend sends results to Plugin));
    I --> J[Plugin displays Score, Issues, Suggestions];
    J --> K[Designer reviews feedback within Figma];
    K --> L{Make Design Changes?};
    L -- Yes --> M[Designer adjusts Figma design];
    M --> E; %% Option to re-run audit
    L -- No --> N{Export Report?};
    N -- Yes --> O[Clicks 'Export Report'];
    O --> P((System: Backend generates PDF/Notion Report));
    P --> Q[Designer downloads/views Report];
    Q --> R[Designer shares Report];
    R --> T[End: Feedback received & Report obtained];
    N -- No --> S[Designer continues work];
    B -- No --> S;
    S --> A; 
