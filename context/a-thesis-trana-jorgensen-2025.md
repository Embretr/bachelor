# Benchmark A-Thesis — Trana & Jørgensen (2025)

**Authors:** Elias Trana, Trygve Jørgensen
**Title:** ChatSSB: Developing LLM-Oriented Techniques to Semantically Retrieve Statistical Data
**Institution:** NTNU, Department of Computer Science
**Supervisor:** Ali Alsam (also our supervisor)
**Submitted:** May 2025
**Industry partner:** Statistics Norway (SSB)

---

## Why this file is here

Second benchmark thesis from our supervisor's pool, kept alongside `a-thesis-amundsen-remoy-2025.md`. **Not a citation source** for our thesis (different topic). Loaded for structural and stylistic comparison.

This thesis is **structurally much closer to ours** than the Amundsen & Remøy one:

- Same supervisor (Ali Alsam)
- Same paradigm: Design Science Research with Peffers DSRM applied through six activities
- Same artefact-plus-knowledge contribution shape
- Eight named iterations of construction (we also have eight)
- Multi-engine benchmark (they compared LLMs across configurations; we compare solvers)
- Sustainability Awareness Framework (SusAF) chapter (we use SusAF too)
- User testing with mixed user groups
- Industry partner relationship (SSB ↔ Admmit)
- "Considering an Official Implementation" section bridges from validation to evaluation

Use this file when comparing DSR structure, iterative-development narration, or evaluation-framework choices. Use `a-thesis-amundsen-remoy-2025.md` for prose voice and Ch 1 structural moves.

---

## Key A-grade signals (transferable lessons)

Different from Amundsen & Remøy because this thesis sits in our methodological neighbourhood. The transfer is about structure, not voice.

1. **DSR Artifacts table (Table 5.9) at end of Results.** Explicit table categorising every artefact produced by the project under Gregor & Hevner's four DSR categories: Construct, Model, Method, Instantiation. ~14 artifacts named. This makes the DSR contribution legible at a glance and gives the reviewer a single place to assess what knowledge the project added. **We do not have this**. Adding a similar table to our §4.x Findings or §5.x Discussion would strengthen the DSR claim significantly.

2. **Three named project requirements (Stability, Efficiency, Security) introduced in §1.1 and answered explicitly in §6.1 Primary Findings.** Same pattern as our three anchors (Efficiency, Control, Adaptability). Each requirement gets its own §6.1.x sub-paragraph that says exactly how the project did or did not meet it. We do something similar in §5.1.1/§5.1.2/§5.1.3, but theirs is more compact and ruthless — each requirement gets one paragraph, not a whole subsection.

3. **Iterative Development chapter (§4.4) is the heart of the method chapter.** Nine named iterations (4.4.1 "All at Once" through 4.4.9 "Retry on failure"), each told as a short narrative: what was tried, what failed, what the fix was, what the next iteration changed. **Code listings embedded in iteration prose** show exact schemas and prompts. We have eight iterations using description-list format; their flowing-prose-with-code-listings approach is an alternative shape worth comparing.

4. **§4.5 Evaluation framework is asymmetric on purpose**, just like our §3.6. They state: "Therefore, the iterative development process from initial prototyping to the finalized techniques are covered in great detail" — and mean it. Their §4.5.1 distinguishes between "techniques" (LLM-agnostic functional building blocks) and "configurations" (technique + LLM combinations). This separation maps cleanly onto our distinction between artefact element (e.g., HITL) vs anchor (e.g., Control). The terminology is different; the structural move is the same.

5. **§6.2 Evaluation Precautions** is a *sharply* honest section. Four sub-paragraphs naming precisely what the evaluation cannot prove (benchmark question scope artificially aligned, selection-accuracy metric edge cases, user-test averages skewed by 4-minute timeout, sample size of two attempts per config insufficient for statistics). This is L1-L12 territory done at chapter level instead of as a forwarded register. Worth comparing to our §5.6 limitations approach.

6. **§6.3 Deviations** — two named deviations from the original plan (lessened security focus, shift of research-question scope). We have something similar in §5.5; theirs is two paragraphs total. Compact.

7. **§6.6 Possible Statbank API Improvements** is a chapter section that turns the project's experience into actionable recommendations for the industry partner (SSB). Three sub-paragraphs: expose subfolders, expose additional table metadata, semantic table indexing. **We do not have this section**. Adding "Recommendations for Admmit" or "Recommendations for the Norwegian transport software market" as a §5.x or §6.x section would convert our learning into something the industry partner can act on.

8. **§6.7 Considering an Official Implementation** explicitly bridges the validation-vs-evaluation gap (Wieringa). Sub-sections on privacy, ethics around bias, societal shift, and immediate applicability (the human-in-the-loop telephone-support deployment scenario). For us, this maps to "What would deployment of RP at one of the seven interviewed companies look like?" — a section we don't currently have, and one that would do real work bridging L6 (no production deployment) to a credible deployment narrative.

9. **§7.1 Conclusion answers each research question verbatim**, with the question quoted as a sub-heading and the answer beneath. We do this in §6.2 with our SQ1/SQ2/SQ3 structure. Theirs is identical pattern; validates that ours is the right shape for an A-grade DSR conclusion.

10. **Chapter 8 Societal Impact + SusAF.** Full chapter, separated from Conclusion (Ch 7). Five SusAF dimensions (Social, Individual, Environmental, Economic, Technical) each get a sub-paragraph. We do SusAF in §5.3 Sustainability — a section, not a chapter. Theirs gives sustainability more prominence; might be a structural move worth considering, though our chapter count would grow.

11. **Code listings embedded directly in method prose (§4.4).** They show actual schemas (Zod, JSON), system prompts (Norwegian and English), and TypeScript interfaces. The reader can verify exactly what the LLM was instructed to do. We have iteration descriptions but no inline code. For us this would mean showing the constraint-provider Kotlin code, the lex-tier scorer config, or a typical Timefold solver invocation as a code listing in §3.5.x or §4.5.x.

12. **Tables for quantitative results (Tables 5.1-5.5).** "Top 5 configurations by accuracy", "Top 5 by speed", "Top 5 by cost", "Top 5 by normalized performance". This is exactly the table format we should consider for our multi-engine benchmark in §4.5.

---

## What does NOT transfer (and why)

- **Their requirements (Stability/Efficiency/Security) are project-side; ours (Efficiency/Control/Adaptability) are anchors emerging from the empirical work.** Surface similarity, deeply different structural roles. Do not collapse the two.

- **Their evaluation framework is symmetric** (technique × LLM = configuration; benchmark every combination). Ours is asymmetric on purpose: §3.6 explicitly tests Efficiency directly while leaving Trust/control and Adaptability as forwarded validation work. We should not adopt their full-grid evaluation matrix; ours fits the DSR validate-vs-evaluate distinction better.

- **Their automated configuration testing scales because comparing LLMs is cheap and fast.** Our equivalent (multi-engine benchmark across three solvers + three datasets) is heavier; we cannot run 54 configurations × 10 questions × 2 trials. Our single-sample wall-clock framing is the honest version of what their multi-trial averaging does.

- **Their user testing is the central evaluation instrument.** Ours is L8 — a known absence. We will not be running user tests in the time remaining; their structure is aspirational only.

- **Their "Lessened Security Focus" deviation** is honest but specific to LLM-anxiety. Our security/ethics surface is smaller; the equivalent deviation for us is L8 (no user testing of the override flow), which we already name.

- **The Conclusion + Further Work + Societal Impact split into Ch 7 + Ch 8** vs our 6-chapter structure with Sustainability inside Ch 5. Theirs adds a chapter; ours folds it in. Both are valid; restructuring to add Ch 7 Societal would be a major move.

---

## Where the comparison helps us

Two clear next-step candidates:

1. **Add a DSR Artifacts table** somewhere in the Findings or Discussion. We have eight iterations + a multi-engine benchmark + a requirements traceability matrix + an interview corpus + the L1-L12 register. Naming each as a Construct/Model/Method/Instantiation per Gregor & Hevner makes the DSR contribution visible at a glance.

2. **Add a "Recommendations for Admmit / for the Norwegian transport software market" section.** Their §6.6 turns project experience into actionable industry recommendations. For us, this could include: expose more configurable hard constraints to the per-company config layer, document the lex-tier scoring scheme as a reusable pattern for VRP variants, etc.

Both are bounded additions that strengthen the thesis without restructuring the spine.

---

## Structural inventory

- 8 chapters: Introduction & Relevance, Theory & Relevant Literature, Background, Method, Results, Discussion, Conclusion & Further Work, Societal Impact
- 77 pages + extensive appendix (xix pages)
- Method chapter has 9 named iterations (4.4.1 - 4.4.9) of the artefact construction
- Results chapter has DSR Artifacts table (5.9) explicitly categorising contributions
- Discussion has 7 sections: Primary Findings, Evaluation Precautions, Deviations, Development Methodology, Teamwork, Possible API Improvements, Considering Official Implementation
- Multiple code listings embedded in method prose (Zod schemas, JSON schemas, TypeScript interfaces, system prompts in both Norwegian and English)
- 5 tables of quantitative results (top-5 rankings by accuracy/speed/cost/normalized performance)
- 12 figures (mostly user-test response-time bar charts)
- SusAF five-dimension analysis as full Ch 8
- Closing pattern: each research question quoted as a sub-heading, answered in 1 paragraph beneath

---

## Full Text

---

NTNU
Norwegian University of Science and Technology
Faculty of Information Technology and Electrical Engineering
Department of Computer Science
Bachelor's thesis
Elias Trana
Trygve Jørgensen
ChatSSB
Developing LLM-Oriented Techniques to Semantically Retrieve Statistical Data
Bachelor's thesis in Computer Science
Supervisor: Ali Alsam
May 2025

## Abstract

This thesis introduces ChatSSB, an interactive tool that uses large language models (LLMs) to process natural language queries and retrieve objective statistical data from SSB's Statbank. Designed with a focus on efficiency, stability, and security, ChatSSB ensures that only objective data is provided, in accordance with SSB's requirement to avoid subjective interpretation or conversational elaboration by the LLM.

By simplifying access to public data, the tool broadens usability for non-technical users. Developed through an iterative design science methodology, ChatSSB features a user-friendly interface, rich visualizations, and multiple LLM-driven data retrieval techniques. Testing with users of varied technical backgrounds showed significantly faster task completion, on average in half the time compared to SSB's traditional interface. Results provide insights into LLM performance with the Statbank API and inform future improvements.

## Sammendrag

Denne oppgaven introduserer ChatSSB, et interaktivt verktøy som bruker store språkmodeller (LLM-er) for å behandle naturlige språkforespørsler og hente statistiske data fra SSBs Statistikkbank. Utviklet med fokus på effektivitet, stabilitet og sikkerhet, sørger ChatSSB for at kun objektive data blir levert, i tråd med SSBs krav om å unngå subjektiv tolkning eller samtalerelaterte utdypelser fra LLM-en.

Ved å forenkle tilgangen til offentlige data, øker verktøyet brukervennligheten for ikke-tekniske brukere. Utviklet gjennom en iterativ designvitenskapelig metodikk, har ChatSSB et brukervennlig grensesnitt, detaljerte visualiseringer og flere LLM-drevne teknikker for datainnhenting. Testing med brukere med varierende teknisk bakgrunn viste betydelig raskere oppgaveløsning, i gjennomsnitt på halvparten av tiden sammenlignet med SSBs tradisjonelle grensesnitt. Resultatene gir innsikt i LLM-ens ytelse med Statistikkbankens API og bidrar til fremtidige forbedringer.

## Preface

From idea to finished project, this experience has been a pleasure for us both. The potential societal impact of creating an application that could positively affect how the entire Norwegian public interacts with statistics, was a driving force during research and development.

We wish to thank SSB for agreeing to collaborate. Having the privilege of collaborating with the source of the inspiration, was a huge motivator for the project. We also wish to thank August Nicolai Meland at SSB for letting us use the name ChatSSB.

We wish to thank Grethe Sandstrak, our Program Manager in our Bachelor of Engineering in Computer Science, for the three years of guidance. We also extend our gratitude to Mehran Raja and Johannes Finsveen at SSB for sharing their expertise on the technologies utilized at SSB, guiding our prioritization, and providing valuable feedback throughout our development process.

Lastly, we especially wish to thank our advisor, Ali Alsam, for great discussions regarding methodology and research, delightful conversations, and incredible guidance for how to write a proper scientific paper.

Elias Trana   Trygve Jørgensen

## Task Description

This thesis aimed to develop an application that simplifies access to official statistics by leveraging LLMs to interpret natural language queries and retrieve the most relevant data. It set out to investigate the feasibility of using LLMs to navigate the data available in SSBs database, with the objective of creating a solution that balances efficiency, stability, and security. The insights gained through this research set out to contribute to potential improvements of the SSB API, making it better suited for integration with LLMs.

## Contents

1 Introduction and Relevance
1.1 Requirements (Stability, Efficiency, Security)
1.2 Research questions
1.3 Acronyms

2 Theory and relevant literature
2.1 Large Language Models (Landscape, Hallucinations, Prompt engineering, Structured output, Tool calling, Agents, RAG, Vulnerabilities)
2.2 REST APIs
2.3 Statistical Definitions
2.4 Sustainability Awareness Framework
2.5 Relevant Literature

3 Background
3.1 SSB and the Statbank (APIs, PxWebApi, PxWebApi 2.0 Specifications, Folder structure, Existing UI)
3.2 LangChain

4 Method
4.1 Defining the Task
4.2 Method Theory (Research Methodology, Application Objectives, Agile Process)
4.3 Choice of Technologies
4.4 Iterative Development Process (9 named iterations)
4.5 Evaluation (Evaluated techniques, Automated configuration testing, User Tests)

5 Results
5.1 Scientific Results (Data Collection and Processing, Automated Test Empirical Findings, User Tests Empirical Findings, Product artifacts)
5.2 Engineering Results
5.3 Administrative Results

6 Discussion
6.1 Primary Findings
6.2 Evaluation Precautions
6.3 Deviations
6.4 Development Methodology and Technology Choices
6.5 Teamwork and collaboration
6.6 Possible Statbank API Improvements
6.7 Considering an Official Implementation

7 Conclusion and Further Work
7.1 Conclusion
7.2 Further Work

8 Societal Impact
8.1 Holistic System Perspective
8.2 Sustainability Awareness Framework

---

## 1. Introduction and Relevance

> "Official statistics are the nation's common factual basis and are essential for a living democracy."
> — SSB, 2025

Statistics Norway (SSB), established in 1876, is a professionally autonomous institution responsible for the collection, compilation, and dissemination of official statistics in Norway. Although it reports to the Norwegian Ministry of Finance, SSB maintains full professional independence in determining what data is published, as well as the timing and methods of publication. With this responsibility, SSB prioritizes maintaining a high level of public trust by ensuring the high quality and integrity of all statistics, research, and analyses it produces. SSB communicates its statistics and research findings through various publications. These curated outputs are tailored to align with the organization's mission of providing the general population with accessible and relevant data.

While these publications are well suited for the common reader, they inevitably cannot capture all the nuances embedded within the raw datasets, nor is it feasible to produce publications that comprehensively cover all the data managed by SSB. To ensure transparency, SSB offers public access to its raw data and associated statistics through the Statbank, a repository containing more than 7000 tables. Users can navigate the Statbank via a user interface that requires traversing a vast hierarchical folder system and accurately selecting relevant parameters for specific tables. This multi-step process is cumbersome, presents usability challenges and in some cases hinders data retrieval, especially for non-technical users.

Large language models (LLMs) are an emerging technology, with new techniques and applications being proposed at a rapid pace. One promising area is LLM-integrated data retrieval, which has already demonstrated considerable value. This project focuses on enhancing the accessibility of SSB's data by developing ChatSSB, an application that interfaces with the Statbank API using LLMs with tailored retrieval techniques. ChatSSB enables natural language querying, automatically retrieves relevant data, and presents it graphically. To guide the development of ChatSSB and evaluate its potential benefits, specific requirements were defined to focus the application's scope and provide insights into what a future official implementation could look like.

Through iterative development and user testing, ChatSSB is shown to offer a significantly promising improvement in how users interact with statistical information. By integrating LLMs and advanced retrieval techniques, the application enables users to quickly find and visualize relevant data, even when seeking hyper-specific information not usually available in standard SSB publications. ChatSSB can particularly benefit non-technical users, individuals with literacy challenges, and speakers of other languages, achieving retrieval speeds as fast as five seconds and offering a far smoother and more intuitive user experience.

Looking toward future improvements, it is clear that systems such as the Statbank API were not originally designed for interaction with LLMs. To optimize the user experience further, changes to the API are proposed to better accommodate LLM-driven queries. This project highlights the viability of using LLMs for guided data retrieval from the Statbank API and points to several promising avenues for enhancing the system in the future.

### 1.1 Requirements

Through discussions with the system architects at SSB, it was agreed that the applications design should follow constraints that would be relevant, were SSB to actually implement such a feature. To evaluate the success of the application, three requirements were set:

**1.1.1 Stability.** The application should consistently return highly relevant data in response to user queries, provided that the requested data exists within the Statbank. In addition, the application should exhibit predictable behavior where semantically similar queries should yield consistent or identical results.

**1.1.2 Efficiency.** Different LLMs present tradeoffs between their speed, intelligence and cost (ArtificialAnalysis, 2025b). As the project will function as a benchmark exploring different retrieval techniques and language models, optimal configurations which best balance the mentioned attributes must be identified.

**1.1.3 Security.** As a publicly trusted institution, SSB must adhere strictly to principles of neutrality, ensuring that its services and publications avoid introducing unintended interpretations of the data. The use of third-party LLMs introduces the risk that generated responses may include interpretations, opinions, or speculative content that could be mistakenly attributed to SSB. Such risks, along with other concerns inherent to the use of LLMs, should be mitigated.

### 1.2 Research questions

Because SSB's project requirements emphasize a balanced focus on stability, efficiency, and security, the primary research question centers on evaluating the viability of LLM-guided data retrieval as a means of fulfilling these criteria. Subsequently, a range of retrieval techniques will be benchmarked to determine which delivers optimal application performance. Once the evaluation is complete and the configuration of LLMs for interaction with the Statbank API has been analyzed, there will be provided targeted recommendations on how SSB might adapt its API to facilitate improved navigation by LLMs.

1. To what degree does LLM-guided data retrieval adhere to the project requirements on the Statbank API?
2. What configurations, like model choice and retrieval techniques, are best suited for optimal application performance?
3. How can the Statbank API be improved to better allow for the usage of LLM navigation?

### 1.3 Acronyms

AA – Artificial Analysis; API – Application Programming Interface; DRS – Design Science Research; DSRM – Design Science Research Process Model; JSON – JavaScript Object Notation; LLM – Large Language Model; RAG – Retrieval Augmented Generation; SSB – Statistics Norway.

---

## 2. Theory and relevant literature

### 2.1 Large Language Models

A Large Language Model (LLM) is a type of artificial intelligence based on a neural network which both takes text as input and gives text as output. Today, LLMs are able to reason, plan and do decision making, all on the basis of a comprehensive semantic understanding (Naveed et al., 2024).

#### 2.1.1 Current LLM Landscape

The landscape of LLMs is rapidly evolving, with hundreds of models now publicly available. Consequently, rigorous scientific analyses of the most recent models are often lacking. However, in recent years, several intelligence benchmarking frameworks have been developed, enabling systematic and generalized evaluations of new models (ArtificialAnalysis, 2025a). These evaluations are essential for model selection, as they provide a reference for expected performance.

As noted in ArtificialAnalysis, 2025c, no single LLM is universally superior. Selecting an appropriate model requires balancing factors such as intelligence, speed, and cost. For example, at time of writing o4-mini (high) ranks highest in intelligence and is approximately 10 times more expensive and 2.7 times slower than the fastest alternative, DeepSeek R1 Distill Qwen 1.5B. However, the intelligence benchmark shows that o4-mini (high) scores 51 percentage points higher intelligence than DeepSeek R1 Distill Qwen 1.5B. The optimal model choice depends therefore on the specific trade-offs between accuracy, cost, and computational efficiency for a given task.

| Model | AA Intelligence Index | USD/1M tokens (Blended) | Tokens/s (Median) |
|---|---|---|---|
| o4-mini (high) | 70 | 1.93 | 143.3 |
| DeepSeek R1 Distill Qwen 1.5B | 19 | 0.18 | 384.0 |

**Table 2.1:** Comparison between the most intelligent and the fastest LLM option available according to ArtificialAnalysis, 2025d.

With LLM API-providers utilizing hardware acceleration, they can offer extreme speeds with demanding LLMs. The fastest available option is at the time of writing the Llama 4 Scout model hosted by Cerebras achieving 2772.9 tokens per second, being 19 times faster than o4-mini (high) while only scoring 27 percentage points less in intelligence (ArtificialAnalysis, 2025c).

#### 2.1.2 Hallucinations

The term hallucination describes cases in which LLMs produce content that is nonsensical or unfaithful to the provided source content (Ji et al., 2023). When relying on LLMs for business logic rather than conventional deterministic algorithms, hallucinations present a significant risk, as they may compromise system reliability if not effectively mitigated.

#### 2.1.3 Prompt engineering

Prompt engineering has gained widespread attention with recent advancements in LLM technology. A prompt refers to any textual input provided to an LLM, serving as the primary mechanism for guiding its generative process. Given that LLMs are inherently capable of producing diverse and unconstrained text, the practice of structuring prompts to elicit specific, controlled outputs, commonly referred to as prompt engineering, has become essential.

By carefully designing prompts like specifying output length and providing example responses (OpenAI, 2025), it is possible to steer the model's behavior, enhance predictability and facilitate practical applications, such as ensuring that outputs conform to standardized data formats for downstream processing.

#### 2.1.4 Structured output

Several leading LLM API providers offer structured output interfaces. In addition to a text prompt, the query is presented with a corresponding JSON schema, which constrains the model's output to conform to the specified structure. This approach functions as an additional prompt engineering step to elicit well-structured responses.

While the internal mechanisms enabling this behavior are generally not publicly documented, it is notable that structured output interfaces do not guarantee that a response will be a valid instance of the schema. This suggests that the functionality may rely on a combination of fine-tuning the model to follow constraints and post-processing the generated output.

#### 2.1.5 Tool calling

Tool calling (or function calling) builds on the idea of structured outputs by allowing models to produce arguments for external functions based on a predefined schema. The LLM's output is parsed according to this schema and used as input to a function, the output of which can be fed back into the model.

This enables dynamic interaction between the LLM and external systems, providing access to real-time data, computational tools, or databases. The model can thus act as a controller or a reasoning layer over programmatic functions, significantly expanding its capabilities beyond static text generation.

#### 2.1.6 Agents

With tool calling allowing LLMs to dynamically retrieve information and interact with digital environments, LLMs can act as autonomous agents. These agents can terminate execution once a goal is achieved or continue operating indefinitely, depending on the task and configuration.

The agents often leverage a toolkit of callable functions alongside components for memory management and planning. This enables the agent to perform extended, multi-step tasks that go beyond the limitations of the LLM's native context window.

#### 2.1.7 Retrieval Augmented Generation

A notable limitation of large language models (LLMs) lies in their inability to access information not present in their training data. This becomes particularly problematic when dealing with post-training knowledge, niche domains or proprietary and private data.

Retrieval-Augmented Generation (RAG) addresses this issue by integrating external knowledge sources into the LLM's inference process. In a typical RAG pipeline, relevant information is retrieved, either directly based on the input query or via a retrieval tool invoked by the model, and injected as contextual input prior to generation.

Most RAG systems rely on vector databases to perform semantic similarity search, identifying documents or textual chunks most relevant to the query. Empirical research has demonstrated that RAG-based approaches produce more accurate, grounded, and informative responses compared to results obtained solely on the model's pre-trained parameters (Lewis et al., 2021).

**Vector Databases and Embeddings.** A vector database is designed to store and query high-dimensional vectors, which are often derived from more complex data types such as text, images, or audio called embeddings. Such embeddings are lower-dimensional representations that capture semantic or structural properties of the original data. In the context of RAG systems, embeddings are typically generated using machine learning models trained to map similar inputs to nearby points in vector space. By embedding new data it can be compared to existing entries using similarity metrics (e.g., cosine similarity or Euclidean distance). This enables efficient semantic search and is widely used in tasks such as reverse image lookup, document retrieval, and natural language search (Taipalus, 2024).

#### 2.1.8 LLM Vulnerabilities

With the increasing adoption of LLMs, vulnerabilities that can be exploited both before and after training have emerged as significant security concerns, as discussed in Yao et al., 2024.

Since an LLM's behavior is inherently shaped by its training data, malicious actors may deliberately manipulate the data corpus, called adversarial attacks, to induce behaviors that diverge from the LLM's intended purpose. This threat is particularly real given that vast portions of the internet are commonly scraped to construct training datasets.

Inference attacks aim to extract general sensitive information about the LLM or its training data by crafting specific queries and analyzing the model's responses. Extraction attacks, in contrast, seek to obtain precise and often private data that may appear in training corpora, such as personal identifiers.

Instruction tuning attacks target LLMs that have been fine-tuned or configured with system prompts to restrict certain behaviors. These attacks attempt to bypass safety constraints embedded during the tuning process.

Finally, bias and unfairness exploitation refers to instances where LLMs either unintentionally perpetuate or can be prompted to express prejudiced or discriminatory outputs.

### 2.2 REST APIs

Representational State Transfer (REST) is a system architecture commonly used for designing APIs in modern web services (Masse, 2011). In a REST API, the client sends an HTTP request that contains all necessary information for the server to process it. This results in a stateless system where the server does not maintain session state between requests.

REST principles, such as a uniform resource structure and strict adherence to the HTTP protocol, make it a popular choice for CRUD (Create, Read, Update, Delete) applications the core functionality centers around databases.

### 2.3 Statistical Definitions

**2.3.1 Statistical Variable.** A statistical variable is a measurable or countable characteristic of a unit within a population. Examples include age, height, or income.

**2.3.2 Categorical Variable.** A categorical variable partitions observations into distinct groups based on qualitative attributes. Examples include gender, housing type, and geographic area. Subdivided into Nominal Variables (no inherent order, e.g. blood type, color) and Ordinal Variables (logical order, e.g. educational level).

**2.3.3 Units.** A unit type refers to the group of entities or cases about which statistics are collected. For instance, in SSB's usage, each individual is considered a unit of the type Person (SSB, 2024).

### 2.4 Sustainability Awareness Framework

The Sustainability Awareness Framework (SusAF) works as a tool for sustainably designing software products and services (SUSO Academy, n.d.). It helps software stakeholders systematically identity and reflect on how a socio-technical system may affect sustainability. The different impacts are split into direct, enabling and systemic. These are further divided on five sustainability dimensions: individual, social, environmental, economic and technical. The process involves a trained moderator guiding stakeholder through a workshop, using diagrams and other tools to find potential impacts, with the goal of building a shared vocabulary for sustainability trade-off and support design choices that take broader sustainability concerns into account.

### 2.5 Relevant Literature

The field of LLMs is continuously evolving with vastly different applications and techniques being developed at a rapid pace. Therefore, current literature offers predominantly general insights, with the project's precise domain being largely unexplored.

**2.5.1 The Original ChatSSB.** *Enhancing Accessibility to Statistical Data through an Open-Source Chatbot Integrated with Language Models*, informally referred to as ChatSSB, was an earlier attempt to enable natural language access to SSB's statistical data (Meland, 2023). Developed during a hackathon hosted by SSB, it shared a similar high-level goal with this thesis. The prototype combined both open-source and proprietary language models, utilized the LangChain library, and was built as a Streamlit web application that allowed users to query the Statbank via a text input field. While the project appears similar at first glance, there are substantial differences in implementation. For instance, the hackathon prototype supported only English queries, lacked integrated graphing or visualization capabilities, and employed different design principles. Nevertheless, the presentation of this work provided valuable insights into the strengths and weaknesses of earlier approaches, informing the development of this thesis.

**2.5.2 Gorilla.** Gorilla is a finetuned LLaMA model with the goal of improving the effectiveness of LLMs utilizing APIs. It handles topics of having LLMs reason to achieve an understanding of the necessary API-calls. It uses self-instruct, fine-tuning and document retrieval to enable LLMs to accurately select from a large, overlapping, and changing set of tools expressed using their APIs and API documentation (Patil et al., 2023). Its relevance to this project can be seen in its dealings with having an LLM understand a user query and use it to generate an accurate API call, as well as dealing with large API structures.

**2.5.3 Self-RAG: Learning to Retrieve, Generate, and Critique Through Self-Reflection.** This thesis implements a retrieval pipeline where the same language model decides when to retrieve, how many times to retrieve and whether its own answer is sufficiently supported. During decoding, the model can emit a special type of token they have defined as reflection tokens. These trigger a passage-retrieval module, meaning it may skip retrieval entirely or retry by iterating multiple times (Asai et al., 2023). After an answer has been produced, it will enter a second reflection phase that critiques both the retrieved evidence and the draft text, allowing the model to revise unsupported claims. The purpose of the framework is to raise the factual accuracy and citation precision, while also avoiding unnecessary API calls.

**2.5.4 Prompting Is Programming: A Query Language for Large Language Models.** Language Model Query Language frames prompting as programming. It describes its functionality as allowing a developer to write a single "query script" that can freely mix natural language fragments with control-flow commands and hard constraints. At compile time, the LMQL turns that script into an optimal decoding procedure that enforces the constraints while minimizing the amount of paid tokens (Beurer-Kellner et al., 2023). This is supposed to cut API costs by 25-80 percent compared to normal prompting. The goal of the language is to provide a declarative, type-safe layer to guarantee that an LLM's reply conforms to a JSON schema or another structural rule-set without extra post-processing.

**2.5.5 A Comprehensive Survey of Hallucination Mitigation Techniques in Large Language Models.** This paper maps the state of the art for mitigating hallucinations. It works as a catalog, showing 32 mitigation methods and groups them along the whole generation pipeline (Tonmoy et al., 2024). This includes pre-generation, retrieval-based, constrained decoding, post-generation and reinforcement/feedback loops. It takes all stages and tags each method by resource needed, task type and compute cost.

---

## 3. Background

### 3.1 SSB and the Statbank

#### 3.1.1 APIs

SSB has three working APIs, namely:

- **REST API with Static Classifications and Codelists:** Provides easy access to metadata across different statistics while ensuring data is standardized, up-to-date, and accurate.
- **API with Pre-made Datasets:** Hosts 210 updated datasets with fixed URLs, compiled from the most frequently accessed Statbank tables.
- **PxWebApi:** Allows for interfacing with all 7,000 Statbank tables, offering complete access to SSBs entire published dataset.

#### 3.1.2 PxWebApi

PxWebApi, often referred to simply as PxWeb or PxApi, is an HTTP-based protocol designed specifically for interfacing with data in the Px-standard, a statistical data format widely adopted by the statistical agencies of Finland, Sweden, Denmark, and Norway. Unlike general-purpose APIs that support CRUD operations, PxWebApi is purpose-built for querying and retrieving statistical data. At present, SSB maintains two separate implementations of PxWebApi: the legacy PxWebApi 1.0, which provides stable access to the Statbank, and the newer PxWebApi 2.0, which is currently in beta.

#### 3.1.3 PxWebApi 2.0 Specifications

The PxWebAPI 2.0 offers several API categories, with most endpoints accessible via HTTP GET requests.

**Endpoints.** The `/navigation` endpoint represents the hierarchical structure of the Statbank. The `/tables` endpoint enables direct access to the entire collection of Statbank tables. To access metadata for a specific table, the endpoint `/tables/<id>` provides a basic subset, while `/tables/<id>/metadata` returns the full metadata. The endpoint `/tables/<id>/data` is used to retrieve actual data from a table, based on selected parameters.

**Table Format and Data Selection.** Each table is structured around dimensions or variables. Every table includes exactly one time variable and exactly one ContentCode variable. To construct a valid query, all mandatory and any relevant optional variables must include selected values. The PxWeb API provides several mechanisms: item selection, wildcard `*`, question mark `?`, top/bottom expressions, range/from/to expressions.

Example query:
```
/tables/07459/data?valueCodes[Tid]=[Range(2010,2020)]&valueCodes[ContentsCode]=Personer1
&valueCodes[Region]=0301,4601&valueCodes[Alder]=05?&valueCodes[Kjonn]=*
```
This addresses: "How many men and women in their fifties lived in Oslo and Bergen municipalities between 2010 and 2020?"

#### 3.1.4 Statbank folder structure

The Statbank contains over 7000 tables, making its folder structure both complex to define and challenging to navigate. The folder hierarchy typically extends to four levels, terminating in a collection of active tables. At the root level, the Statbank is divided into 23 main categories based on broad societal themes. While this enhances discoverability for human users, it can introduce challenges for programmatic navigation.

#### 3.1.5 Existing User Interface

SSB has a query tool on its website that allows users to search for tables based on keywords. Areas where the search engine struggles arise when a user treats it like a conventional search engine rather than as a keyword lookup. SSB offers a non-compromising interface for variable selection when a table is selected. All available values in every single variable are directly listed.

### 3.2 LangChain

LangChain is a modular framework designed for building applications powered by LLMs. It provides a unified and extensible API that abstracts over different model providers, whether through hosted APIs or self-deployed models, allowing developers to implement text generation and other LLM-driven functionalities using a consistent interface (LangChain, 2025b).

**3.2.1 BaseChatModel.** The standardized structure through which supported LLMs can be integrated.

**3.2.2 Callbacks.** When initializing a BaseChatModel, callback functions can be defined to execute at specific checkpoints during model invocation.

**3.2.3 Structured Output.** LangChain offers the `.withStructuredOutput()` method, which binds a JSON schema to a model and automatically parses outputs into valid JSON objects (LangChain, 2025c).

**3.2.4 Additional Functionality.** LangChain also includes a suite of standardized components for advanced LLM use cases, including tool usage, short-term and long-term memory management, agent-based workflows (now extended into the LangGraph library), multi-modal inputs, retrieval-augmented generation, and evaluation mechanisms based on LLM feedback.

---

## 4. Method

> "The study of scientific method is the attempt to discern the activities by which that success is achieved. (...) Activities commonly identified as characteristic of science include systematic observation and experimentation, inductive and deductive reasoning, and the formulation and testing of hypotheses and theories."
> — Hepburn & Andersen, 2021

### 4.1 Defining the Task

The idea to enhance access to statistical data using natural language emerged from the authors' own experience navigating the SSB website, particularly the Statbank interface. Challenges in manually locating relevant datasets prompted the exploration of a potential solution that leverages the capabilities of LLMs.

To find out whether such a solution could be of interest to SSB, the authors initiated contact through the organization's general inquiry webpage. After seven days, a response was received, leading to a productive dialogue with SSB's system architects. During this conversation, it became clear that SSB had previously conducted experimental integrations of LLMs with the Statbank API. However, those earlier efforts had demonstrated limited capability, particularly when handling complex or nuanced queries.

Through these dialogues, the core requirements efficiency, stability and security originated, which became central to one of the thesis's research questions. Once a mutual understanding of the thesis had been established, efforts turned toward examining their previous initiatives and researching the utilized technologies. Finally, ChatSSB was proposed as a fitting name for the application, as an homage to ChatGPT.

With a concept, requirements, and a name in place, the next step was to develop a thorough understanding of the Statbank API. This process involved studying the Statbank's hierarchical folder structure, table metadata and analyzing all relevant documentation. Building upon this foundational knowledge, further insights were obtained through discussions with SSB regarding the PxWebApi 2.0 which at the time was in beta. This collaboration enabled the application to integrate the most up-to-date technologies available at SSB.

A review of papers utilizing LLMs with APIs, different types of RAGs, hallucination mitigation and other relevant techniques, was conducted (§2.5). In order to structurally attain knowledge, the Design Science Research framework was the baseline for the iterative development process.

Following the iterative development process, promising techniques were evaluated through empirical testing, yielding quantitative results. This data was then used to analyze and compare configurations, with the aim to identify high performers. A distinct configuration would then serve as the basis for user testing, comparing the time usage between the standard SSB website and ChatSSB, while observing qualitative user behavior.

### 4.2 Method Theory

#### 4.2.1 Research Methodology

Design Science Research (DSR) is a problem-solving paradigm that seeks to expand human knowledge within the domain of information systems by creating innovative artifacts (Hevner et al., 2004). An artifact is defined as a product of the research process and may be either tangible or conceptual.

DSR contributes to both technological and scientific knowledge bases by developing artifacts that address real-world problems and improve their operational contexts. A DSR project aims to extend human and organizational capabilities through the design of novel artifacts, which are typically categorized as constructs, models, methods, and instantiations (Gregor and Hevner, 2013).

DRS comprises three foundational cycles: relevance, design, and rigor. The relevance cycle aligns the research with authentic organizational or societal needs. The design cycle encompasses the iterative development and refinement of artifacts, which are assessed based on predefined goals. The rigor cycle embeds the research in established theoretical frameworks and extends the existing knowledge base through validated contributions (Hevner et al., 2004).

This thesis leverages LLMs to navigate the Statbank API, while adhering to the requirements listed in §1.1. The project adopts a DSR approach: iteratively building artifacts, evaluating their strengths and weaknesses through rigor, and incorporating those insights into subsequent iterations.

DSR is the ideal paradigm for this work because it combines artifact construction with theory development. In contrast, a purely positivist approach seeks objective laws through hypothesis testing and statistical analysis, maintaining researcher detachment from the intervention (Eidlin, 2015). An interpretivist approach, by contrast, focuses on understanding actors' subjective meanings through immersion in context (Alharahsheh and Pius, 2020). DSR bridges these perspectives by actively creating an artifact while simultaneously generating design theory about its effectiveness and impact.

**DSRM Process Model.** The Design Science Research Methodology provides a structured framework for conducting design science research by defining the principles, practices, and procedures necessary to ensure both methodological rigor and practical relevance (Peffers et al., 2007). The steps utilized are Problem identification and motivation, objectives of a solution, design and development, demonstration, evaluation and communication.

**Applied Process Model.**
- *Problem Identification and Motivation:* The problem was identified through observations that attempting to retrieve data from the SSB website proved challenging.
- *Objectives of a Solution:* In consultation with SSB architects requirements for efficiency, stability, and security were defined.
- *Design and Development:* A web application supporting user interaction was developed, and various retrieval techniques were evaluated through an iterative design process.
- *Demonstration:* The completed application integrates the designed techniques and LLMs, successfully retrieving the desired statistical data.
- *Evaluation:* Quantitative benchmarks were conducted to measure accuracy, response time, and cost for each viable configuration. Qualitative user tests with participants of varying expertise were also performed.
- *Communication:* Recommendations for future work and suggested enhancements to the SSB Statbank API are presented, grounded in empirical benchmarks, user feedback, and practical experience.

#### 4.2.2 Application Objectives

As the application aims to address the real world constraints an official implementation would imply, a set of concrete objectives were set in place:

- The interface should be user friendly.
- User input is handled through a singular text field.
- All responses should include all relevant contextual data.
- All responses should include SSBs designated table ID from which the data were fetched.

#### 4.2.3 Agile Process

To align with the iterative principles of DSRM, the project followed an agile development process. To maintain clarity and coordination, work was divided into milestones and sprints, with each sprint containing a list of issues, which were managed and delegated through GitHub. Each sprint concluded with a review and retrospective.

### 4.3 Choice of Technologies

**4.3.1 Typescript and Next.JS.** To enable rapid development and deployment of the web-application which would serve as the testing platform, a Next.js and Vercel stack were employed. TypeScript, being an established choice for web-development, was chosen for its robust type-safety to standardize the data passed in API fetches between the LLM and SSBs Statbank.

**4.3.2 D3.js.** D3.js is a free, open-source JavaScript library for building custom data visualizations from low-level primitives rather than pre-configured chart types. Leveraging native web standards such as SVG and Canvas ensures efficient in-browser rendering, and its data-binding model allows for adding, removing or updating variables dynamically.

**4.3.3 LangChain.** As the project aims to compare the performance of different LLMs, it requires connecting to different API-providers. LangChain removes the need to rewrite all LLM business logic for each specific provider.

**4.3.4 Prototyping LLM.** OpenAI's GPT-4o-mini served as the prototyping LLM in early development, primarily because it was perceived to strike a strong balance between intelligence, speed, and cost.

### 4.4 Iterative Development Process

Research questions 1 and 3 both require qualitative analysis of the development process in order to gain valuable insights. Therefore, the iterative development process from initial prototyping to the finalized techniques are covered in great detail.

#### 4.4.1 All at Once

The first attempt for navigating from a user query to a relevant statistical table relied on a generated overview provided by SSB, covering the top three levels of the Statbank folder hierarchy. This structural metadata was formatted as a single JSONL string containing 50258 tokens. The LLM was given basic instructions to extract the most relevant folder ID, based on the assumption that its natural language understanding would suffice to parse and filter relevant information from such a verbose data format.

This approach had several major flaws. Mainly, the sheer volume of unprocessed data overwhelmed the capabilities of the 4o-mini model, often resulting in hallucinated outputs. Furthermore, due to the inclusion of folder IDs from all three hierarchy levels, the LLM frequently returned IDs from non-target folders. Additionally, this method depended on a static snapshot of the folder structure, lacking the necessary adaptability needed in an actual implementation.

#### 4.4.2 From Query to Data

**Folder Navigation.** Recognizing the need for careful prompt engineering and aiming to reduce the contextual load on the LLM, a revised approach was implemented that interfaces directly with the PxWebApi. This approach leveraged the `/navigation` endpoint where each Statbank folder lists its contents as clearly defined JSON objects with labels and IDs. Rather than parsing a full structure in a single prompt, the technique presents folder contents incrementally, asking the LLM to select the most relevant ID at each step. This choice then triggers retrieval of the next folder level, repeating the process until a final data table is reached. Notably, the root folder only required 1390 tokens in raw JSON, significantly lowering the prompt size.

The recursive navigation approach successfully enabled the LLM to autonomously navigate folders and fetch tables, achieving consistent results without hallucinating or producing invalid IDs. The average end-to-end execution time was roughly 10 seconds, primarily due to latency between folder-level decisions.

A major issue presented itself as the selected tables, in some instances, did not match the semantic intent of the user's query. This limitation reflects the difficulty of leveraging LLMs when faced with vague folder labels.

**Primitive Value Selection.** The PxWebApi offers optional programmatic tools for value selection within table variables. The first approach avoided utilizing these tools, expecting to reduce complexity, and thereby hallucinations. The approach involved presenting the LLM with the available set of values and instructing it to return the most relevant one, resulting in another "copy-paste" strategy.

While this method successfully produced valid selections, its limitations quickly became evident. When the LLM is constrained to select specific values through this literal "copy-paste" approach, requesting large sets such as the last 30 years of data, can result in excessively long query strings, potentially exceeding the PxWebApi's 2500-character limit for GET requests.

#### 4.4.3 Enhance Functionality While Maintaining Simplicity

**Parallel Folder Navigation.** The initial folder navigation technique had a key limitation: it allowed the LLM to select only one folder at a time, with no mechanism to undo suboptimal choices. To address this, the LLM was instructed to select the top n most relevant folders. The backend would then fetch the contents of these folders, merge their entries into a single list, and present them to the LLM as if they came from one unified folder.

The parallel navigation technique showed an immediate improvement over single folder navigation, although increasing n from 3 to 4 or 5 did not appear to significantly change accuracy, even though its time usage increased due to the increased token input.

**Expression Selection Technique.** The initial selection technique was deprecated due to its limitations in handling large value ranges. A new approach was introduced: feeding the PxWebApi documentation to the LLM and instructing it to generate a valid expression. This strategy relies on the LLM's understanding of the documentation, eliminating the need for manual syntax validation.

This approach was yet another improvement uncovering new problems. The LLM was now able to select large sets of values using concise expressions, significantly enhancing the flexibility of the selection process. However, the LLM could sometimes misuse the selection expressions syntax, resulting in invalid GET requests.

#### 4.4.4 Absolute Constraints

Allowing the LLM to construct its own selection expressions inevitably introduces a persistent risk: since an LLM can generate any arbitrary string, there is always the possibility of producing an invalid expression, regardless of the LLM's intelligence. Recognizing that structured output mechanisms are specifically designed to address such issues, an alternative approach was pursued with the goal of defining a schema that would eliminate any output that could result in an invalid GET request.

In practice, this approach did not eliminate failed requests. Instead of returning invalid API calls, the LLM often failed to produce a valid schema at all, resulting in schema fulfillment errors. This was largely due to a sharp increase in token usage due to the enumerated constraints that required repeating the entire value set for each constrained field.

#### 4.4.5 Tentatively Comparing LLMs

Although selection could still be optimized, it became necessary to assess how different LLMs performed under the current setup, ensuring the design did not implicitly favor the GPT-4o-mini model. Observations across the latest LLMs available from OpenAI, Google, and Groq showed that navigation was achievable even with smaller LLMs. However, selection tasks proved to be too contextually taxing.

This illustrated that the process should be properly split into two distinct stages: navigation, defined as mapping a user query to the appropriate table, and selection, which involves extracting data from the selected table based on the query. By doing so, the system could capitalize on the speed and cost-efficiency of smaller LLMs where they perform adequately, while delegating the more complex selection phase to larger, more capable LLMs.

#### 4.4.6 Coming to Terms with LLM's Volatility

Ultimately, the Enum technique failed to ensure schema validity, even with top-performing reasoning LLMs like GPT-o4-mini, which led the ArtificialAnalysis rankings at the time. This highlighted a core limitation: no matter how capable the LLM, schema-constrained output could not always guarantee a valid GET request.

Given this, a more pragmatic strategy was adopted based on the principle that an imperfect answer is better than none. In many cases, LLMs produced well-formatted outputs containing invalid values. By identifying and replacing these invalid entries with wildcards, all possible values for the given variable would be selected and it became possible to salvage responses while eliminating the need for strict enumerated constraints.

#### 4.4.7 Leveraging Language and Creating New Context

Norwegian and English instructions were inconsistently mixed across several techniques. Although LLMs have built-in translation layers, research suggests they primarily think in English (Zhao et al., 2024). To reduce ambiguity and leverage the LLM's stronger proficiency in English, all instructions, as well as the language parameter in the Statbank API, were set to English.

To mitigate the lack of descriptive metadata in the Statbank API, a reasoning step was added at the very beginning. The LLM is prompted to follow a structured analysis, including translating the user query into English and enriching it with contextual reasoning. This enhanced prompt is then used alongside the original query during the navigation and selection phases.

#### 4.4.8 A New Approach to Navigation

The navigation segment, though effective, was inefficient as it required invoking the LLM at least 5 times. Using the `/tables?query=<string>` endpoint, a keyword search returns up to 20 tables with matching metadata, ranked by a basic semantic engine.

The Keyword Search technique allows the LLM to generate several relevant keywords from the query, each triggering an independent search. The results are merged, and the LLM selects the most relevant table from the combined set. This ensures broader coverage so long as one keyword matches a relevant table, it will be included for final selection.

#### 4.4.9 Retry on failure

Both the navigation and selection steps rely exclusively on structured output for every LLM invocation. However, no LLM reliably guarantees schema validity, meaning a single invalid schema causes the entire process to fail. A `parsableRetryWrapper()` was implemented. It appends the error message to the original instruction set, informing the LLM of the schema violation and prompting it to retry. This process repeats until a valid schema is produced, with a maximum of five attempts.

While this does not ensure a valid result, testing showed that many retries successfully corrected earlier errors, significantly reducing the number of failures.

### 4.5 Evaluation

To effectively evaluate individual segments or the application as a whole, it is important to clearly distinguish between techniques and configurations.

**Techniques** refer to isolated functionalities responsible for specific aspects of the data retrieval process. They are not bound to any particular LLM. **Configurations**, on the other hand, represent the integration of a specific technique with a designated LLM.

#### 4.5.1 Evaluated techniques

Both navigation techniques, **Folder Navigation** and **Keyword Search**, were tested in three configurations, each defined by a navigation value of 1, 3, or 5.

All three selection techniques were evaluated. The **Expression** technique lets the LLM freely generate selection expressions, which may result in syntax errors or invalid values, even with a valid schema. The **Enum** technique restricts schemas to predefined enumerated values, ensuring all valid schemas produce valid GET requests. The **Redundant** technique allows potentially invalid values but guarantees valid requests by handling them programmatically through filtering or broadening the selection.

#### 4.5.2 Automated configuration testing

10 benchmark questions were created that represent a varied set of queries users could ask for, from basic and popular information, to niche and specific data. Since the application operates through distinct steps, each is tested in isolation to identify the most effective configuration for that stage.

Each test involved prompting all configurations with the set of 10 benchmark questions, conducted across two isolated runs. This yielded a total of 20 results per configuration.

**Reasoning** was excluded from automated testing and instead was simulated using a predetermined reasoning text appended to each question prompt.

**Navigation** evaluation. For each question, two lists of tables were defined. The `expectedCorrectTables` include tables that both accurately describe and contain data needed to answer the question. The `technicallyCorrectTables` contain relevant data but are labeled in a way that makes their contents non-obvious. Selecting a table outside these two lists is considered incorrect, while failing to select any table is classified as an error.

**Selection** evaluation. Each question was associated with a specific table, simulating the result of a navigation step selecting that table. When a configuration selects values from the table's metadata, results based on correct values, extra values, and missing values is collected for each variable.

#### 4.5.3 User Tests

The user tests aim to compare how participants retrieve data using the SSB website versus ChatSSB, focusing on time usage, perceived difficulty, and instances of confusion.

All sessions were recorded. Time usage will be analyzed as quantitative data, whereas observed user experiences will contribute to the qualitative analysis.

**Users.** The test included participants with diverse levels of technological and statistical expertise. The median user group consisted of students, representing the average user. To evaluate accessibility, individuals with limited digital proficiency were included, while expert users from SSB illustrated the optimal use of the SSB website.

**Questions.** All questions were confirmed to be accessible on both platforms and were designed to always yield a correct response from ChatSSB when queried verbatim. Questions 1 and 4 expects favourability for SSB (commonly asked queries well-supported by SSB homepage), whereas questions 2, 3, and 5 would align more closely with ChatSSB's capabilities (niche or obscure data).

| Nr. | Original (Norwegian) | Translation |
|---|---|---|
| 0 | Oppvarming: Hvor mange mennesker bor i Norge i dag? | Warm-up: How many people live in Norway today? |
| 1 | Hvor mange hadde fornavnet Åsne i 2024? | How many people had the first name Åsne in 2024? |
| 2 | Vis et linjediagram av hvor mye øl som ble solgt de siste 100 årene | Show a line chart of how much beer was sold over the last 100 years. |
| 3 | Hvor mange minutter ser folk på tv i løpet av en dag i året 2000 versus 2024? | How many minutes do people watch TV in a day in the year 2000 versus 2024? |
| 4 | Hva var gjennomsnittlig årslønn i 2020? | What was the average annual salary in 2020? |
| 5 | Hvor mange elektriske biler har blitt solgt de siste 5 årene? | How many electric cars have been sold in the last 5 years? |

---

## 5. Results

### 5.1 Scientific Results

#### 5.1.1 Data Collection and Processing

**Speed and Cost.** Milliseconds and input tokens were recorded for each question during automated testing. To ensure fairness in evaluation, test results where a configuration produced an error were excluded.

**Navigation Accuracy.** Each navigation test instance was categorized into one of four classes: correct, technically correct, incorrect, or error. Accuracy was defined as the average proportion of successful responses (correct + technically correct) across all test instances.

**Selection Accuracy.** Each successful selection test included a list of variables, where each variable was assigned counts for correct (c), extra (e), and missing (m) values. The percentage accuracy per variable: A = c / (e + c + m) · 100%. The configuration's overall accuracy score was computed as the average of these percentages.

**Normalized Relative Performance.** All metrics were treated with equal weight and normalized. Each configuration was assigned a normalized score along three axes (speed, cost, and accuracy) forming a position in a three-dimensional metric space. The Euclidean distance to the ideal point was then calculated. A distance of 0 represents the absolute best configuration, while 1 is the worst.

#### 5.1.2 Automated Test Empirical Findings

**Navigation Configuration Evaluation.** Out of the 54 configurations tested, none emerged as universally dominant across all evaluation metrics.

| Model | Technique | Avg. time (s) | Accuracy (%) | Avg. cost ($) |
|---|---|---|---|---|
| GPT-4.1 | Keyword S. 5 | 13.54 | 100 | 0.014049 |
| Gemini Flash 2 | Folder Nav. 3 | 22.94 | 95 | 0.000912 |
| GPT-4.1 Mini | Folder Nav. 5 | 13.86 | 95 | 0.004168 |
| GPT-4.1 Mini | Folder Nav. 3 | 10.55 | 90 | 0.003465 |
| GPT-4.1 | Folder Nav. 5 | 19.80 | 90 | 0.020841 |

**Table 5.1:** Top 5 configurations by accuracy.

Llama 4 Maverick led in speed, averaging just 0.82 seconds from query to table. Gemini Flash 2 Lite with Keyword Search 1 proved to be the most economical, costing on average 105 times less than the most expensive configuration. Measuring the normalized relative performance, **Gemini Flash 2 with Keyword Search 5** topped the chart by a noticeable margin.

| Model | Tech. | Avg. time (s) | Accuracy (%) | Avg. cost ($) | Norm. Dist |
|---|---|---|---|---|---|
| Gemini Flash 2 | Keyword S. 5 | 5.61 | 85 | 0.000809 | 0.0898 |
| Llama 4 Scout | Keyword S. 5 | 1.06 | 70 | 0.00076 | 0.1057 |
| Llama 4 Scout | Keyword S. 3 | 1.45 | 70 | 0.000533 | 0.1058 |
| GPT-4.1 Mini | Keyword S. 1 | 1.72 | 70 | 0.000984 | 0.1069 |
| GPT-4.1 | Keyword S. 1 | 3.14 | 80 | 0.004894 | 0.1091 |

**Table 5.4:** Top 5 navigation configurations by normalized performance.

**Selection Configuration Evaluation.** In stark contrast from the navigation evaluation, a single selection configuration delivered the best performance in all measurable metrics, achieving a perfect normalized relative performance score. That configuration was **Gemini Flash 2 using the Redundant technique**, closely followed by GPT-o4-mini, also with the Redundant technique.

| Model | Tech. | Avg. time (s) | Accuracy (%) | Avg. cost ($) | Norm. Dist |
|---|---|---|---|---|---|
| Gemini Flash 2 | Redundant | 1.08 | 89.58 | 0.000833 | 0 |
| GPT-o4-mini | Redundant | 3.87 | 88.42 | 0.007682 | 0.041 |
| Qwen QWQ 32B | Redundant | 5.47 | 75.83 | 0.004186 | 0.091 |
| Llama 4 Maverick | Expression | 1.59 | 74.93 | 0.001415 | 0.092 |
| Llama 4 Maverick | Redundant | 1.88 | 74.55 | 0.002214 | 0.095 |

**Table 5.5:** Top 5 selection configurations by normalized performance.

#### 5.1.3 User Tests Empirical Findings

The total configuration utilized for user tests:
- **Reasoning:** On
- **Reasoning LLM:** GPT-4.1
- **Navigation Technique:** Keyword Search 5
- **Navigation LLM:** GPT-4.1
- **Selection Technique:** Redundant
- **Selection LLM:** GPT-o4-mini

**Students.** Students completed the tasks significantly faster using ChatSSB than with SSB. SSB required approximately 2.5x the time per task compared to ChatSSB (101.4s vs 41.73s on average across Q1-Q5).

**Experts.** ChatSSB outperformed SSB on questions 2, 3, 4, and 5, whereas SSB showed quicker results for question 1. The time differences here were less dramatic. Overall slight average speed advantage for ChatSSB across expert users (69.93s vs 51.33s).

**Non-technical users.** Across all questions, non-technical users were consistently slower on the SSB website and in many cases were not able to find the requested data within 4 minutes. Overall: SSB 179.6s vs ChatSSB 55.07s.

**Combined Results.** The combined results across all user groups show a consistent time advantage for ChatSSB over SSB (SSB 116.98s, ChatSSB 49.37s overall average). Non-technical users demonstrated the largest discrepancy. Notably, students performed faster than experts on ChatSSB, while experts outpaced students when using SSB.

#### 5.1.4 Product artifacts (Table 5.9: Design Science Research Artifacts)

**Constructs**
1. *Elaboration-Free Data Retrieval* — Only factual numbers are presented, prohibiting the LLM from introducing misinformation.
2. *Text-box to Data* — The concept of going directly from query to the exact relevant data.

**Models**
1. *ChatSSB System Logic* — The complete process of going from query to table to data.
2. *Type Schema Mirroring* — Designing schemas that mirror the Statbank API.
3. *Streaming Backend Logs* — When a query is handled, data is streamed to the frontend to allow for real time updates.
4. *PxWebApi-Oriented Instruction Prompts* — Precisely describing proper variable value selection.

**Methods (Navigation)**
1. *Keyword Search (1–5)* — Utilizing Statbank Search to locate relevant tables.
2. *Parallel Navigation (1–5)* — Navigating the Statbank by going from root folder to relevant table.

**Methods (Selection)**
3. *Redundant* — Programmatically handling invalid values. Simple and robust.
4. *Enum* — Absolute constraints of the structured output. Contextually heavy.
5. *Expression* — LLM designs its own selection expression. Relies entirely on LLM intelligence.

**Methods (Other)**
6. *Single Value Display Widget* — Showing precise information if value is singular.
7. *Real-time Navigation Stream* — Showing the user how the system navigates.
8. *Wildcard Fallback* — When a parameter selection technique fails, its automatic fallback is to select all available elements within that category.
9. *Retry on Failure* — Wherever a structured output is required, a failure will trigger a retry, up to 5 times.
10. *Navigation and Selection Separation* — Using different techniques and LLMs on different steps.
11. *Dev Mode Tools* — Allowing users to customize the setup with details about results.
12. *Empirical Tests* — Tests measuring speed, accuracy and cost of different techniques and configurations.
13. *Streamlit Website* — A website with all empirical test results that allows for user customization.
14. *User tests* — User tests comparing SSB to ChatSSB.

**Instantiation**
1. *ChatSSB Web Application* — The full complete iteration of ChatSSB.

### 5.2 Engineering Results

#### 5.2.1 Final Application

Upon opening the ChatSSB web application, users are presented with a brief introduction to its features, along with three demo questions they can select. A persistent input field at the bottom of the screen allows users to enter new queries at any time. Once a query is submitted, real-time updates from the navigation process are streamed to the frontend, providing users with insight into the paths and options the LLM is exploring.

When a relevant table is identified, the backend initiates the selection process. The response then presents the user either with a single numerical value or a set of values in a bar chart, with additional visualization options available.

**Fullscreen Mode.** Whenever a response consists of a set of values, Full-Screen Mode allows the user to get an enlarged view of the data. Here, built-in tools can perform linear regression analysis on separate categories of the given data. This mode works as a proof of concept, and is therefore kept to a minimum.

**Dev Mode.** To allow for rapid testing of different configurations, techniques and LLMs can be hot swapped in the Dev Mode interface. When querying a specific configuration, both time and token usage is tracked giving an immediate overview of speed and cost.

#### 5.2.2 Qualitative User Test Observations

A notable trend among students and non-technical users was the tendency to treat the SSB website's search bar as though it could interpret natural language, often resulting in no search results and user confusion. These groups also showed a preference for browsing SSB articles rather than engaging directly with the Statbank.

While the source tables are consistently referenced within the articles, users rarely interacted with them. In contrast, expert users demonstrated more efficient navigation of the SSB website, particularly when selecting variable values in tables or adjusting data visualizations.

### 5.3 Administrative Results

#### 5.3.1 Scheduled Progress

The scheduled progress plan was followed precisely according to the planned structure. Each large deadline and sprint were placed in a Gantt diagram to visualize the progress towards the finalized project.

#### 5.3.2 Time Tracking

To keep track of the time usage, all work was logged in a Google Sheet table, with date, hour and type of work being displayed. For each week, a concise status report was written.

#### 5.3.3 Process Documentation

GitHub Milestones organized the iterative design process. Each milestone contained issues pertaining to the sprint, allowing progress tracking and task delegation. Sprints had a sprint plan with broader focus, plus issues for specific ideas. Each sprint concluded with review and retrospective.

Issuebranching: Each created issue had a branch, created from the newest instance of either Main or Dev. This setup allowed for the lean and fast paced development process.

For every meeting, both with the advisor at NTNU and collaborators at SSB, meeting agendas were sent. After each meeting, this document would be utilized as a meeting minutes document.

---

## 6. Discussion

### 6.1 Primary Findings

**Regarding Stability.** In comparing the various configurations, the most advanced LLMs currently available demonstrate a degree of accuracy that is both promising and arguably sufficient to fulfill the Stability requirement. With certain configurations achieving 100% accuracy in navigation and 90% in selection, ChatSSB demonstrates a reliable ability to retrieve data on behalf of the user, provided that the requested data exists in the Statbank.

**Regarding Efficiency.** With respect to the Efficiency requirement, even without official estimates from SSB regarding acceptable cost thresholds, selecting an optimal configuration necessitates careful consideration. While the most accurate navigation configuration achieves an average cost of $0.014 per query, the second-most accurate option operates at a mere $0.0009. When scaled to accommodate hundreds of thousands or even millions of queries, this order-of-magnitude price difference would significantly affect the total operational expenses.

Application speed varies considerably, ranging from near-instantaneous responses of 2-3 seconds to delays of up to 60 seconds in the least efficient configurations. Notably, across both navigation and selection tasks, Gemini Flash 2 consistently ranks highest in normalized relative performance. While it achieved the highest measured selection accuracy, it curiously underperforms in perceived answer relevance when compared to GPT-o4-mini outside the automated tests. This discrepancy suggests that GPT-o4-mini's inherent reasoning capabilities may confer an advantage when handling high contextual loads.

**Regarding Security.** Since the Statbank is inherently public and ChatSSB leverages external LLMs without fine-tuning or memory, LLM-related vulnerabilities such as adversarial, inference, and extraction attacks are functionally avoided (Yao et al., 2024). No sensitive information is input into the system unless voluntarily provided by the user.

Except for the reasoning step, all LLM outputs are constrained to a defined schema, and this structured output is used for programmatic execution. This design ensures that instruction-based attacks, such as prompt injections, cannot compromise system integrity.

The principal remaining risk is that of bias and unfairness which is a concern acknowledged since the project's inception and one that continues to pose the most significant barrier to a formal implementation. Unless one assumes the possibility of absolute neutrality, an idea debated for humans (Sukhera, 2019) and even more so for machine learning models (Kumar et al., 2025), bias remains inevitable.

### 6.2 Evaluation Precautions

**6.2.1 Benchmark Question Scope.** For the automated tests, all benchmark questions were meticulously constructed by the authors to ensure it included all the necessary contextual information required to both locate the appropriate table within the Statbank and to identify the correct variables and their values for selection. In this controlled setting, the questions were designed to describe data that was known to exist in the Statbank. However, this level of alignment between user queries and actual database content is unlikely to occur frequently in real-world usage. The performance metrics serve primarily as a comparative tool, not absolute indicators.

**6.2.2 Selection Accuracy Metric.** When collecting selection data, sampling the number of extra values may initially appear irrelevant. While users can technically ignore these values when they receive a response, it is essential to acknowledge that many of SSB's tables include variables with a vast number of possible values. For example, the table "10501: Persons, by first name, contents and year" contains 2123 unique names. If a user submits a query to retrieve data on the usage of their own name over the past 10 years, applying a wildcard to the name variable will present the user with a chart containing 21230 bars, making the output virtually impossible to interpret.

**6.2.3 User Test Skewed Averages.** The user test imposed a maximum time limit of 4 minutes, after which any ongoing attempt was terminated. The timeout occurred only once for students and never among experts, however it was relatively common among non-technical users, occurring a total of six times, all when using the SSB website. These timeouts were included in the average as 240-second values, thereby skewing the average towards smaller values. In reality, these users would likely have taken much longer.

**6.2.4 Lack of Data.** Even though many different configurations were tested, each one only answered the same 10 questions twice. Despite configuring all LLMs with a temperature setting of 0, intending to make responses fully deterministic, results still varied between runs. A sample size of only two attempts per question is insufficient to draw statistically significant conclusions. Substantially larger sample sizes would be required to reliably characterize the performance and stability of each configuration.

### 6.3 Deviations

**6.3.1 Lessened Security Focus.** Initially, security was a central design concern, driven by the perceived risks of prompt injection attacks and other potential vulnerabilities. However, because development immediately decided on an architecture centered around structured outputs with strict programmatic handling that would only interface with the public PxWebApi, such concerns quickly subsided. What was originally expected to be a development process heavily shaped by ongoing security considerations instead shifted focus. Only the issues of bias and unfairness remained as a notable concern.

**6.3.2 Shift of Research Question Scope.** Initially, the research sought to examine how LLMs could be used to navigate and utilize web APIs in general. However, it became clear that web APIs differ widely in structure and implementation, limiting this projects potential for generalizable solutions. This realization led to a revised focus on the Statbank API alone. Importantly, because the Statbank API conforms to the PxWebApi standard, the conclusions drawn retain relevance for other systems utilizing the same standard, even outside of SSB.

### 6.4 Development Methodology and Technology Choices

**6.4.1 Effects of Agile Process and DSR.** Using larger sprints guided by general milestones allowed the team to work with flexibility, treating milestones more as navigational aids than strict rules. Each sprint included tasks inspired by broader objectives, but there was room for adjustment. Utilizing the concepts of Design Science Research Methodology, and especially the Process Model already fit naturally into the rapid iterations environment, allowing for retrospective mapping of the process to the specific steps defined in DSRM. With specific artifacts, the learnings in this project are more clearly defined, allowing for proper integration into the global knowledge base.

While the iterative development process was crucial for achieving a usable outcome, it lacked an empirical foundation to guide successive iterations. Many decisions were made without quantitative backing, as approaches were predominantly assessed qualitatively through informal testing rather than via consistently measurable metrics.

**6.4.2 Impact of Technology Choice.** The final codebase, comprising both the application and the test scripts, serves as a centralized platform for continued experimentation and evaluation of future LLMs. LangChain played a key role in enabling efficient comparisons across API providers, though its reliance on generalized interfaces imposed certain limitations. TypeScript's type safety proved particularly valuable as data could hold a predetermined format between LLM generated structured outputs, the Statbank API and visualization modules.

The development process was however constrained by an external factor: the Beta version of the PxWebApi is inactive during weekends due to its ongoing development status. Consequently, coding and API-related tasks had to be concentrated on weekdays, while weekends were dedicated to writing the thesis.

### 6.5 Teamwork and collaboration

Given the team consists only of the two authors, collaboration was necessarily close-knit and dynamic. Teamwork was characterized by a combination of dedicated work ethic and a shared commitment to maintaining a balanced workload, with particular attention to avoiding burnout. The project's foundation in a real-world case, with implications for the future operations of SSB and, by extension, how the public accesses statistical information, served as a strong motivational factor for both participants.

By leveraging each individual's strengths, where one focused on the backend and the other on frontend, both were rewarded with efficient autonomy, all while every design choice was discussed in detail.

### 6.6 Possible Statbank API Improvements

As instructed by SSB, during development there was also made an effort to demonstrate how the Statbank API could be significantly enhanced to better support LLM-driven applications. It is important to emphasize that these proposed improvements are not grounded in empirical measurements but are instead based on practical experience.

**6.6.1 Expose Subfolders.** When interacting with the `/navigation` endpoint, exposing the subfolders contained within each `FolderInformation` object would provide significantly more context, possibly enabling LLMs to better pick relevant folders. A simple list of subfolder labels would suffice. While this functionality is technically achievable by programmatically retrieving the contents of every folder and formatting the relevant information, doing so would require a substantial number of API calls, resulting in inefficient usage and unnecessary load on the SSB servers.

**6.6.2 Expose Additional Table Metadata.** In both the Folder Navigation and Keyword Search approaches, the only information currently available prior to table selection includes the table's label, covered timespan, and variable names. Exposing additional metadata, such as table notes, variable sizes, and relevant codelists, could further aid the LLM into making better table choices.

**6.6.3 Semantic Table Indexing.** As the project seeks to integrate automatic semantic understanding with a semantically static data source, current approaches have primarily involved wrapping LLM techniques on top of the Statbank API. The emergence of vector databases and sophisticated embedding models provides a viable path forward. Modern embedding models make it possible to represent each table with a semantic vector. These embeddings can then be indexed, allowing for fast and meaningful semantic search across all 7000 tables. Such a system could significantly reduce, or even eliminate, the need for the LLM during the navigation phase.

### 6.7 Considering an Official Implementation

**6.7.1 Privacy Concerns.** Deploying an official implementation similar to the current application implies that user queries, potentially containing sensitive information, will be processed through a LLM. If this LLM is hosted by an external API provider, there is a risk that such sensitive data may be stored or exploited by that third party. Several powerful LLMs, such as the LLaMA series and DeepSeek models, are available as open-weight alternatives. These can be hosted locally by SSB, and are natively compatible with ChatSSB through LangChain's support for Ollama.

**6.7.2 Ethics Around Bias and Unfairness.** LLMs inherently involve interpretation, and therefore, some degree of bias is unavoidable. This remains true even in systems such as ChatSSB, where LLM-generated text is not directly exposed to the user. Bias may still manifest indirectly through the LLM's selection of statistical tables or variable values in response to a query. For instance, a seemingly neutral query like "boring jobs" could prompt the LLM to select data related to accounting. Rather than attempting to eliminate this intrinsic property, which is ultimately infeasible, a more practical and ethically sound alternative is to emphasize transparency.

**Societal Shift.** In discussions with SSB it was pointed out that despite their positive view of the project, they remain cautious about utilizing such an application for official deployment. The mere fact that the LLM must take interpretive choices on behalf of the user is something society as a whole may not be comfortable with accepting. At the same time, increased public access to statistical data, enabled by natural language interfaces such as ChatSSB, could justify a modest tolerance for the risk of misinformation.

**Immediate Applicability.** Due to these ethical concerns, an initial deployment scenario for ChatSSB was identified within SSB's internal telephone support services. Customer service agents could use the system to quickly locate statistical information, while maintaining human oversight to ensure response accuracy. This human-in-the-loop model ensures that responses are validated before being communicated to the public, effectively mitigating the risks associated with LLM reasoning.

---

## 7. Conclusion and Further Work

### 7.1 Conclusion

The project has successfully explored the domain of every research question and the learnings has contributed to SSB's knowledge base.

> **To what degree does LLM-guided data retrieval adhere to the project requirements on the Statbank API?**

With the most advanced LLMs available at the time of writing, ChatSSB has proven sufficient Stability, where further accuracy improvements is expected with model-specific solutions. However, achieving acceptable Efficiency requires careful architectural decisions and may pose challenges for official implementation. Application Security does not appear to be a significant concern, provided that SSB chooses to utilize locally hosted models while only interacting with publicly available APIs. The most persistent challenge remaining is bias and unfairness, which are inherent to LLMs and must be managed accordingly.

> **What configurations, like model choice and retrieval techniques, are best suited for optimal application performance?**

Empirical testing reveals that Gemini Flash 2 outperforms its competitors across relative performance metrics, suggesting that development tailored to this model could be a promising direction. Navigation accuracy appears largely independent of retrieval technique, making Keyword Search the preferred option due to its superior speed. In scenarios requiring large context loads, which is common in the selection step, no LLM has proven immune to hallucinating invalid values. The Redundant technique specifically acknowledges this by programmatically handling these values, achieving superior performance. Continuing to embrace the principle that LLMs are prone to hallucination and designing around this limitation might prove to be a vital design philosophy for future improvements.

> **How can the Statbank API be improved to better allow for the usage of LLM navigation?**

The Statbank API stands to benefit significantly from additional descriptive metadata. Any supplementary semantic information will guide LLMs toward more accurate decision-making, reducing uncertainty during data retrieval. Furthermore, semantically embedding all tables and employing a vector database could be implemented as a true semantic search engine, potentially eliminating the need for LLM-driven navigation entirely and simultaneously improving search functionality on the website itself.

### 7.2 Further Work

**7.2.1 Programmatically Handling Codelists.** Ignoring codelists and presenting all variable values within a single aggregated list has served as a general-purpose solution for various selection techniques. However, in rare cases, certain variables, such as region, may involve extremely large codelists. For instance, the base statistical unit can comprise over 32000 values. Implementing dynamic handling of codelists can not only partition variables into more manageable segments but may also enhance selection accuracy.

**7.2.2 Improved Frontend.** A user profile system could allow users to store and browse previous conversations, as well as creating favorites and or collections of responses. In dialogue with SSB, it was discussed to implement features to facilitate analysis on the retrieved data. This evolved to the full-screen mode where users can perform linear regression on the given data. This illustrates the potential of implementing additional tools like combining data from different tables and organizing their responses for advanced research purposes.

**7.2.3 Increased Testing.** Firstly, all conducted tests should be recreated with considerably increased datapoints with the aim of increasing the reliability of the given results. Focusing the tests on the most commonly asked questions received by SSB could better depict the real-world relevance of the results. Future tests should be explorative, yielding more insight into user behavior and satisfaction.

---

## 8. Societal Impact

### 8.1 Holistic System Perspective

ChatSSB can be seen, not as a standalone tool, but as a broader sociotechnical system of data retrieval, dissemination and use. SSB collects and curates official statistics that are published to the Statbank API. ChatSSB takes natural-language queries, uses them to create relevant API calls, sets fitting parameters and presents them to the user. Users of ChatSSB, potentially researchers, journalists or regular citizens, pose questions, consume the answers and react to these answers either by accepting them or modifying their questions. Throughout the use of the application, employees at SSB can monitor the performance, and modify its configuration as needed. ChatSSB operates as a link in a broader system that focuses on providing statistical data to the Norwegian public.

### 8.2 Sustainability Awareness Framework

To assess the societal impact of the project, the Sustainability Awareness Framework is utilized to concretely measure the effects.

**8.2.1 Social.** ChatSSB offers a single, intuitive input field in which users pose questions in natural language. This minimalist interface demands little prior experience with digital tools. By contrast, SSB's existing platform can be overwhelming for non-technical users. In fulfilling SSB's mission to disseminate statistical data to the Norwegian public, ChatSSB can significantly broaden its audience. However, simplifying access to data carries risks. Users may default to the easiest answer rather than the most comprehensive one. Furthermore, the quality of ChatSSB's responses depends on the precision of the user's query. Poorly formulated questions may yield irrelevant or misleading information, potentially propagating misinformation.

**8.2.2 Individual.** People with difficulties around reading and writing can now easily be presented with a summarized dataset that only answers their specific question, without requiring user navigation. As LLMs are processing the users questions, any potential typos or misunderstandings of words or phrases will be understood and taken into account when searching the API for the user. ChatSSB solves the multi-language access problem by allowing the user to ask their question in any language they wish.

**8.2.3 Environmental.** The application's environmental impact will vary vastly based on the chosen model. Efficiency has been central throughout development, resulting in an end product capable of operating on light weight models. The environmental impact of an actively running version of ChatSSB can vary based on where the utilized models are run.

**8.2.4 Economic.** Keeping operational costs low has been a major priority in the development of ChatSSB, particularly because the application must remain free to end users. Even with careful cost minimization, the platform still involves both fixed and variable (per-user) operational costs. Since ChatSSB is built to serve the public using openly available SSB data, there is no commercial incentive driving the project. However, the use of the PxWebApi, which is widely adopted across Scandinavian statistical agencies, opens up opportunities for reuse beyond Norway.

**8.2.5 Technical.** ChatSSB is built on industry standard technologies, with large support bases for further development. It uses open source libraries for its interaction with LLMs, is LLM-agnostic in its operation, and as a whole is developed as a framework that allows for further implementation of modern LLMs and other techniques.

**8.2.6 Effects of Sustainability.** Deploying ChatSSB on the SSB platform is expected to elevate computational demands due to increased reliance on LLMs and API queries. Optimization strategies, such as deploying lightweight models or improving model accuracy, can either lower system strain or reduce redundancy in interactions, respectively. Increased user engagement through ChatSSB could democratize access to statistical data. However, removing the need to manually sort through available data may lead to passive consumption, as users might overlook relevant context not conveyed through the application. Should SSB proceed with the proposed modifications to the Statbank API, such changes could structurally enhance the efficiency of LLM-guided data retrieval.

---

## Bibliography (selected)

Alharahsheh, H. H., & Pius, A. (2020). A review of key paradigms: Positivism vs interpretivism. Global academic journal of humanities and social sciences, 2(3), 39-43.

ArtificialAnalysis. (2025a). Artificial analysis intelligence benchmarking methodology.

ArtificialAnalysis. (2025c). LLM API providers leaderboard.

Asai, A., Wu, Z., Wang, Y., Sil, A., & Hajishirzi, H. (2023). Self-rag: Learning to retrieve, generate, and critique through self-reflection. arXiv:2310.11511.

Beurer-Kellner, L., Fischer, M., & Vechev, M. (2023). Prompting is programming: A query language for large language models. Proceedings of the ACM on Programming Languages, 7(PLDI), 1946-1969.

Bogmans, C., et al. (2025). Power Hungry: How AI Will Drive Energy Demand. IMF Working Paper WP/25/81.

Eidlin, F. (2015). Positivism. In M. Gibbons (Ed.), The encyclopedia of political thought.

Gregor, S., & Hevner, A. (2013). Positioning and presenting design science research for maximum impact. MIS Quarterly, 37, 337-356.

Hepburn, B., & Andersen, H. (2021). Scientific Method. The Stanford Encyclopedia of Philosophy.

Hevner, A., March, S., Park, J., & Ram, S. (2004). Design science in information systems research. MIS Quarterly, 28, 75-105.

Ji, Z., et al. (2023). Survey of hallucination in natural language generation. ACM Comput. Surv., 55(12).

Kumar, C. V., et al. (2025). No LLM is free from bias: A comprehensive study of bias evaluation in large language models. arXiv:2503.11985.

Lewis, P., et al. (2021). Retrieval-augmented generation for knowledge-intensive NLP tasks. arXiv:2005.11401.

Masse, M. (2011). REST API design rulebook. O'Reilly Media.

Meland, A. N. (2023). Enhancing accessibility to statistical data through an open-source chatbot integrated with language models.

Naveed, H., et al. (2024). A comprehensive overview of large language models. arXiv:2307.06435.

Patil, S. G., Zhang, T., Wang, X., & Gonzalez, J. E. (2023). Gorilla: Large language model connected with massive APIs. arXiv:2305.15334.

Peffers, K., Tuunanen, T., Rothenberger, M., & Chatterjee, S. (2007). A design science research methodology for information systems research. JMIS, 24, 45-77.

Sukhera, J. (2019). Can we be consciously unbiased?

SUSO Academy. (n.d.). Sustainability Awareness Framework (SusAF).

Taipalus, T. (2024). Vector database management systems: Fundamental concepts, use-cases, and current challenges. Cognitive Systems Research, 85, 101216.

Tonmoy, S. M. T. I., et al. (2024). A comprehensive survey of hallucination mitigation techniques in large language models. arXiv:2401.01313.

Yao, Y., et al. (2024). A survey on large language model (LLM) security and privacy: The good, the bad, and the ugly. High-Confidence Computing, 4(2), 100211.

Zhao, Y., Zhang, W., Chen, G., Kawaguchi, K., & Bing, L. (2024). How do large language models handle multilingualism? arXiv:2402.18815.

---

## Appendix A: Additional Material (summarised)

Appendix A contains: detailed code examples of the selection-expression system prompt, raw empirical-data result structures (single navigation and selection test results in JSON), the complete navigation and selection performance tables across all 54 navigation and 21 selection configurations, application screenshots (ChatSSB interface, navigation streaming, D3.js graphing, single-value display, Dev Mode, Full-Screen Mode), GitHub milestones for all five sprints, Gantt diagram, issue and branching screenshots, time accounting screenshot, and the SusAD diagram showing the three sustainability impact levels (direct/enabling/systemic) across the five SusAF dimensions.
