# Benchmark A-Thesis — Amundsen & Remøy (2025)

**Authors:** Andrea Amundsen, Julia Vik Remøy
**Title:** Generative AI in Programming Education: Perspectives from Public Discourse, Students and Educators
**Institution:** NTNU, Department of Computer Science
**Supervisor:** Ali Alsam (also our supervisor)
**Submitted:** May 2025
**Grade:** A — described by Ali Alsam as "the best thesis he has ever read"

---

## Why this file is here

This is the benchmark A-thesis from our supervisor's pool. It is loaded into context so future sessions can compare structural and stylistic choices against ours when revising the prose. **It is NOT a citation source** — the thesis topics are entirely different (GenAI in education vs algorithm-assisted resource planning), and Amundsen & Remøy are never cited inside our thesis text. The relevance is the writing voice, structural choices, and methodological discipline that earned the A-grade.

When the user asks "compare to ours" or invokes A-thesis voice / faster prose / less bullshit, look here. Use also when calibrating expectations for what an A-grade NTNU IDI bachelor thesis under Ali Alsam looks like in 2025.

---

## Key A-grade signals (transferable lessons)

Ranked by transferability to our thesis. The full analytical comparison was done in conversation 2026-05-09; key takeaways frozen below.

1. **Faster prose.** Their average sentence is shorter, their average paragraph is shorter, their information-per-word is higher. Opening hits in one sentence; ours took four paragraphs to do equivalent setup work. They trust the reader. We perform completeness.

2. **Visible evidence chain.** Every theory paragraph names a specific paper, what that paper found, and what it implies. §2.1.1 reads "In a first-year programming course, Wu et al. (2025) conducted a controlled experiment where students used ChatGPT as part of a structured peer assessment process..." then the result, then the implication. The reader watches research happen. Our Ch 2 cites well, but the citations more often anchor a frame than report a finding.

3. **Methodological reasoning in front, not behind.** Why this YouTube video? Three named criteria. Why three sentiment models? Each represents a distinct computational approach. Why also manual coding? Models miss sarcasm. Every choice is earned out loud. We assert ("the framework is asymmetric on purpose") and the reader has to take it on faith.

4. **Per-subsection one-line takeaway.** Every results subsection ends with "These results indicate that..." or "These findings highlight..." — a one-line takeaway so the reader knows what to remember. Ours presents findings and trusts the reader to extract the takeaway. The compounded effect across a chapter is large.

5. **Bachelor-genre structural signals.** Their Ch 1 has: §1.1 Problem Definition (single paragraph + RQ list), §1.2 Problem Domain Contributions (bulleted list), §1.3 Thesis Structure (chapter-by-chapter map), §1.4 Additional Resources (links to artefact code/datasets). Each is short and structural; together they tell the reader "you are reading a bachelor thesis" in a recognisable shape.

6. **Closing statement.** "Thank you for reading our bachelor thesis. [Date, City. Signed.]" — the genre's closing convention. Cheap to add.

7. **Heuristic / comparison tables for compact reference.** Their Table 3.3 captures three sentiment models in a two-column "Model | Sentiment Labeling Rule" table. Compact, scannable, replication-friendly.

---

## What does NOT transfer (and why)

- **Mixed-methods data-source-by-data-source Ch 3 structure.** Their Ch 3 organises by data source (literature review, YouTube, survey, interviews). Ours is DSR-organized (defining task, DSRM, data collection, data analysis, iterations, evaluation, validity). The DSR frame requires our structure.

- **Short Discussion (4 pages, just RQ interpretation + limitations).** Ours is justifiably longer because anchor-organized analysis (§5.1 Efficiency, Control, Adaptability), adoption (§5.2), sustainability (§5.3), L1-L12 register (§5.6), deviations (§5.5), and methodology reflection (§5.7) all require space. Ours is structurally richer; not a defect.

- **Personal "we" voice.** Per CLAUDE.md, we use impersonal academic constructions. Don't transfer.

- **Combined Limitations + Future Work in one section.** They do `5.2 Methodological Limitations and Future Work`. We separate into §5.6 (L1-L12 register) and §6.3 (Future Work). Our separation is clearer for a 12-limitation system.

- **Survey-style figures (12 of them).** Appropriate for survey-heavy mixed methods. Ours has benchmark plots; the figure shape doesn't transfer.

- **Topic relevance to Ali.** Their thesis is about programming education — Ali's professional life. He reads it as a participant. Ours is about Norwegian transport coordinators; he reads it as a methodologist. **This we cannot change.** It is structurally locked in by the bachelor task we accepted.

---

## What our thesis does that theirs does not

Worth noting because the contrast validates structural choices that might otherwise feel over-engineered:

- Three locked anchor concepts (Efficiency, Control, Adaptability) spine both Ch 1 and Ch 5. Theirs has thematic categories that emerge from data; ours has concept-locked anchors that organise cross-chapter coherence.
- L1-L12 hierarchical limitations with explicit per-finding forward-pointers from where each limitation originates. Theirs has a single-section limitations paragraph batch.
- Bainbridge + Hoff/Bashir + Miller + Wieringa theory layering with each anchor concept theoretically grounded.
- DSR + DSRM + eight-iteration narrative as the artefact's constructive component. Theirs has no constructive component to compare.
- Multi-engine benchmark with shared time budget, shared scorer, lex tiers, and honest single-sample labelling.

---

## Structural inventory (counted from the source)

- Front matter: Abstract + Sammendrag + Preface (signed)
- 6 chapters: Introduction, Theory, Method, Results, Discussion, Conclusion
- Total ~70 pages
- ~12 prose paragraphs in Ch 1 + 4 bulleted lists (vs our ~22 prose paragraphs, 0 bulleted lists pre-restructure)
- Ch 2 has ONE main section (Related Work) with 4 subsections, ending with explicit "Summary and Concluding Remarks"
- Ch 3 organises strictly by data source
- Ch 4 has 12 figures and 5 tables (survey-heavy)
- Ch 5 is short (4 pages: §5.1 Interpretation by RQ, §5.2 Limitations and Future Work)
- Ch 6 is short (3 pages: synthesis + §6.1 Ethical and Sustainability)
- Closing statement ("Thank you for reading our bachelor thesis. Date, City. Signed.")
- Bibliography, then Appendix A (Jupyter notebook screenshot + dataset link)

---

## Full Text

The full pasted text follows. It includes the abstract, sammendrag, preface, contents, all six chapters, bibliography, and appendix A. Use targeted excerpts when illustrating a specific structural or stylistic point.

---

NTNU
Norwegian University of Science and Technology
Faculty of Information Technology and Electrical Engineering
Department of Computer Science
Bachelor's thesis
Andrea Amundsen
Julia Vik Remøy
Generative AI in Programming
Education: Perspectives from
Public Discourse,
Students and Educators
Bachelor's thesis in Computer Science
Supervisor: Ali Alsam
May 2025

## Abstract

This thesis explores how generative AI is influencing programming education, with a focus on experiences from students, educators, and public discourse. Using a mixed-methods approach, the study combines a literature review, a sentiment and thematic analysis of YouTube comments, a survey among third-year computer science students at NTNU, and interviews with educators and one student. The results show that students use GenAI tools extensively and that many find them helpful for learning and motivation. At the same time, concerns are raised about over-reliance, reduced understanding of fundamental concepts, and changes in how students engage with lectures and exercises. Educators describe both opportunities and challenges in adapting teaching practices to a changing learning environment. Public discourse reflects a broad range of opinions, from optimism about GenAI as a tool to concerns about job displacement and changing skill requirements. The findings provide insight into how programming education is being reshaped by GenAI and reflect about how educational institutions can respond.

## Sammendrag

Denne oppgaven utforsker hvordan generativ kunstig intelligens påvirker programmeringsutdanning, med fokus på erfaringer fra studenter, undervisere og den offentlige diskursen. Ved å bruke en kombinasjon av metoder, består studien av en litteraturgjennomgang, en sentiment- og temaanalyse av YouTube-kommentarer, en spørreundersøkelse blant tredjeårsstudenter i informatikk ved NTNU, og intervjuer med undervisere og én student. Resultatene viser at studenter bruker GenAI-verktøy i stor grad, og at mange synes de er nyttige for læring og motivasjon. Samtidig uttrykkes bekymringer om overdreven avhengighet, redusert forståelse av grunnleggende konsepter, og endringer i hvordan studenter forholder seg til forelesninger og øvinger. Undervisere beskriver både muligheter og utfordringer i å tilpasse undervisningen til et endret læringsmiljø. Den offentlige diskusjonen viser et bredt spekter av meninger, fra optimisme om GenAI som verktøy, til bekymringer om tap av jobber og endrede ferdighetskrav. Funnene gir innsikt i hvordan programmeringsutdanning formes av GenAI, og reflekterer over hvordan utdanningsinstitusjoner kan tilpasse seg.

## Preface

This bachelor thesis serves as the final evaluation for the Computer Science program at the Norwegian University of Science and Technology (NTNU) and builds upon a specialization project conducted during the autumn semester. The topic was selected due to a shared interest in the intersection of artificial intelligence and education, coupled with a desire to understand how generative AI is transforming programming learning environments. The project began with a literature review and gradually expanded into a comprehensive mixed-methods study, incorporating public discourse analysis, a student survey, and interviews with both educators and a student. Working on this thesis has been both intellectually challenging and deeply rewarding, offering new perspectives on a rapidly evolving field.

We would like to extend our sincere thanks to our supervisor, Ali Alsam, for his motivating presence, engaged follow-up, and unwavering support throughout the process. His constructive feedback and clear enthusiasm for the subject matter have been invaluable in shaping both our work and our thinking. We are also grateful to NTNU and all our lecturers for three demanding, formative, and inspiring years of study.

Trondheim, 15/06/2025
Julia Vik Remøy   Andrea Amundsen

## Contents

1 Introduction 1
1.1 Problem Definition
1.1.1 Research Questions
1.2 Problem Domain Contributions
1.3 Thesis Structure
1.4 Additional Resources

2 Theory 7
2.1 Related Work
2.1.1 Opportunities and Challenges of GenAI in Programming Education
2.1.2 Student Engagement With GenAI
2.1.3 New Competencies and Employer Demands
2.1.4 Summary and Concluding Remarks

3 Method 13
3.1 General design of the study
3.2 Literature Review
3.2.1 Search Strategy
3.2.2 Inclusion Criteria
3.2.3 Article Filtering and Selection
3.2.4 Data Extraction and Analysis
3.3 Analysis of YouTube Comments
3.3.1 Analytical Limitations and Design Considerations
3.3.2 Video Selection
3.3.3 Data extraction
3.3.4 Thematic Filtering Using Keyword Groups
3.3.5 Thematic exploration with ChatGPT-4o
3.3.6 Sentiment Classification
3.4 Survey
3.5 Constructing The Interview Guide
3.5.1 Expert Interviews (Process)
3.5.2 Student Interview (Process)

4 Results 31
4.1 YouTube Comment Analysis
4.1.1 Filtering by keywords
4.1.2 Thematic patterns identified by Chat-GPT
4.1.3 Sentiment Classification Results
4.1.4 Distribution of manual Sentiment labeling
4.1.5 Model Agreement with Manual Coding
4.2 Student Survey Results
4.3 Expert Interview Results
4.3.1 Interview with Expert 1
4.3.2 Interview with Expert 2
4.3.3 Interview with Expert 3
4.4 Student Interview Result

5 Discussion 59
5.1 Interpretation of Key Findings
5.2 Methodological Limitations and Future Work

6 Conclusion 63
6.1 Ethical and Sustainability Implications

Bibliography 65
Appendix A Additional Material

---

## 1. Introduction

A student attends an entire semester without opening a textbook, writing a single line of code, or asking a professor a question. Instead, they rely entirely on an AI assistant that reads the curriculum, explains complex concepts, writes code, and helps them prepare for the final exam, all through natural conversation. Just a few years ago, this would have seemed unthinkable. Today, this scenario is a reality.

In 1962, philosopher Thomas Kuhn introduced the idea of paradigm shifts. These are moments when a field must rethink its foundations because the old ways of solving problems and understanding the world are no longer enough (Kuhn, 1962). Generative AI (GenAI) is driving one of the most profound paradigm shifts in technology and society today. It requires a completely different approach to how AI is developed, understood, and applied (Miikkulainen, 2024). Traditional AI was built on clear rules, logic, and transparency, but GenAI systems are too large, dynamic, and complex to fit within those frameworks (Miikkulainen, 2024). These models now take on creative roles in writing, music, art, programming, science, and business. AI is no longer just a tool for solving specific tasks, but is becoming a creative partner transforming industries and society.

Within just five months of the GenAI model ChatGPT's release in late 2022, 500 million users around the world subscribed to it, covering 209 of the 218 countries in the world (See fig. 1.1) (Liu and Wang, 2024). Usage data show that these tools are accessed primarily during weekdays and from desktop devices, indicating that they are being used for work and educational purposes (Liu and Wang, 2024).

GenAI is having a major impact in programming education. Students are increasingly using tools like ChatGPT and Copilot to help them with code suggestions, debugging, and explanations in natural language (Wu et al., 2025; Llerena-Izquierdo, Gómez et al., 2024). These AI systems offer immediate feedback and accessible explanations, making programming tasks easier to approach. However, formal education has not yet fully adapted to this shift. Most programming courses still rely on traditional teaching methods, and there is little systematic integration of AI into curricula (Komp-Leukkunen et al., 2024; Yilmaz and Karaoglan Yilmaz, 2023). Educators face challenges in how to respond to a learning environment where students increasingly depend on GenAI tools. As GenAI becomes more widespread, the ability to critically engage with AI-generated outputs is becoming a necessary skill for future programmers, but academia are still catching up (Groothuijsen et al., 2024).

This uncertainty about how programming education should adapt is echoed by some of the leading voices in the technology industry. Sam Altman, CEO of OpenAI, predicted in an interview with Lex Fridman that "in a few years, coding will be done in natural language" (Fridman and Altman, 2024). Jensen Huang, CEO of NVIDIA, speaking at the World Government Summit, stated that "everybody in the world is a programmer now" and went as far as to suggest that students "should not study computer science," emphasizing that it is NVIDIA's job to create computing technology that "nobody has to program" (Summit, 2024). These bold statements reflect a growing belief that traditional programming skills may soon become less central, replaced by the ability to interact with intelligent systems through natural, human language. If such a future materializes, it would not only redefine what it means to be a programmer but also force academia to fundamentally rethink how programming is taught.

Reaching the final stages of our own computer science education during this ongoing transformation has inspired us to explore the implications more deeply. As students, it is difficult to imagine how traditional programming education can continue unchanged in the face of GenAI. This thesis was motivated by a desire to understand how GenAI is transforming programming education and to provide insights that may contribute to reflections on how academia could adapt to an AI-augmented world.

As will be seen in chapter 2, the existing research landscape is still in an early phase. Most studies rely on small-scale case studies. Few studies examine the broader, structural implications of GenAI for programming education as a whole. Because of these limitations, we have designed a mixed-methods research approach that combines a structured literature review, a survey of computer science students, an analysis of public discourse, and qualitative interviews with both students and experienced programming educators. This combination allows us to move beyond small isolated observations and offer a more comprehensive perspective on how GenAI is transforming this field.

How GenAI influences programming education is a large, global and rapidly evolving case. It spans different educational systems, cultural contexts, and touches on everything from teaching methods and learning outcomes to the role of educators and institutions. The complexity and pace of this transformation make it impossible to fully capture within the scope of a five-month bachelor thesis. Instead, this study focuses on how the shift is experienced by students, discussed in public discourse, and approached by educators. The goal is not to provide definitive answers, but to contribute to a broader conversation and encourage further research and reflection as the field continues to develop.

### 1.1 Problem Definition

This bachelor thesis explore how academia can respond to the challenges and opportunities that generative AI presents in programming education, focusing on its impact as experienced by students, discussed in public discourse, and addressed by educators.

The general definition of the problem guiding this thesis is:

*How is generative AI influencing the learning of programming in higher education?*

To approach this, we addressed the three following research questions:

#### 1.1.1 Research Questions

- **RQ1:** How has the emergence of generative AI impacted programming education?
- **RQ2:** What are the positive and negative effects of using generative AI in programming education?
- **RQ3:** How is generative AI reshaping the skill set required for future developers?

### 1.2 Problem Domain Contributions

This bachelor thesis specifically contributes to the problem domain through:

- A review of the literature on the effects of GenAI in programming education, learning processes, and skill development.
- An analysis of YouTube comments on a highly viewed video, capturing global opinions and concerns about the role of GenAI in programming education.
- A quantitative survey examining how third-year computer science students at NTNU use generative AI tools, and how these tools influence their learning and study habits.
- Interviews with experienced programming educators providing insights into their experiences and reflections on the theme.
- An interview with a first-year computer science student, highlighting the experiences of a new generation studying in the GenAI era.
- A discussion that interprets the key findings in relation to the research questions and critically reflects on methodological limitations affecting the study.

### 1.3 Thesis Structure

Following is an overview of the thesis structure:

1. **Introduction.** Provides an overview of the problem domain, outlines the motivation for the study, the research method, and presents the research questions.
2. **Theory.** Reviews related work on generative AI, programming education, and skill development, with a focus on identifying gaps and limitations to inform our study.
3. **Method.** Describes the methodological approach taken in the study.
4. **Results.** Presents the findings from the various data sources, including the literature review, student survey, expert interviews, student interview, and YouTube comment analysis.
5. **Discussion.** Interprets the findings in light of the research questions and reflects on methodological limitations.
6. **Conclusion and Further Work.** Summarizes key insights, discusses implications for education, and outlines suggestions for future research.

### 1.4 Additional Resources

The full sentiment analysis notebook is available at:
https://colab.research.google.com/drive/1naGbwLSOtrvL8fKbHBKMEqCO3iNrTuWz?usp=sharing

All datasets and results from the YouTube comment analysis are available at:
https://drive.google.com/drive/folders/1fzgot61WV11A2DCoNjNGafz5ktM7nymx?usp=drive_link

This includes:
- Sentiment scores from VADER, TextBlob, and BERT
- Results from manual sentiment analysis
- Outputs from the thematic classification using ChatGPT

---

## 2. Theory

### 2.1 Related Work

The purpose of this section is to provide an overview of existing research on GenAI in programming education. As this is a newly emerging field, the majority of the relevant literature has been published between 2023 and 2025. The review aims to map the current research landscape, identify methodological trends, and highlight gaps that inform the design of this study. A key observation is that most of the studies are small-scale case studies, often limited to short-term classroom experiments. This has become the dominant research approach in the early stages of the field.

The review draws on peer-reviewed articles identified through a structured literature search, described in detail in Chapter 3. These studies span multiple continents, including North America, South America, Europe, Asia, Africa, and Oceania, highlighting the global nature of the field. The findings are structured around the core themes identified in the literature: how GenAI is changing programming education, effects of GenAI on learning and skill development, and new competencies and employer demands. Finally, the section concludes with a discussion of the reviewed literature, focusing on identified limitations and gaps.

#### 2.1.1 Opportunities and Challenges of GenAI in Programming Education

Drawing on recent empirical studies, this section explores how GenAI tools have been introduced in programming education and what effects have been observed. By examining how these tools have been used in specific educational contexts, the section outlines some of the opportunities and challenges currently being discussed in the literature.

Several recent studies demonstrates how GenAI can positively impact programming education when used within structured, well-designed learning settings. In a first-year programming course, Wu et al. (2025) conducted a controlled experiment where students used ChatGPT as part of a structured peer assessment process. Rather than using AI freely, students followed a defined peer-review cycle, using ChatGPT to provide feedback on one another's work. This thoughtful integration of AI led to increased self-efficacy, better understanding of programming concepts, and more meaningful engagement with the material (Wu et al., 2025). Similarly, Llerena-Izquierdo et al. (2024) studied an introductory programming course where students used Gemini, Google's GenAI tool, through the Google Colab coding platform. Students could ask the AI for help while working on exercises. Over 90% reported higher motivation and greater independence, suggesting that access to GenAI tools within familiar environments can enhance learning when used with clear instructional support. These results suggest that when GenAI is embedded intentionally into the curriculum, it can foster self-directed learning, deepen conceptual understanding, and reduce barriers for students who may otherwise struggle (Llerena-Izquierdo, Gómez et al., 2024). Supporting this, Yilmaz and Karaoglan Yilmaz (2023) divided undergraduate computer science students into two groups: one group used ChatGPT to assist with weekly programming lab assignments, while the other group completed the same tasks without access to the tool. The results showed that the ChatGPT group developed stronger computational thinking skills, higher confidence in their programming abilities, and greater motivation to learn (Yilmaz & Karaoglan Yilmaz, 2023). It is important to note that these studies are largely based on students' self-reported experiences and perceptions.

At the same time, other research highlights important risks associated with the use of GenAI tools in programming education. A mixed-methods study by Groothuijsen et al. (2024) examined how Master's students in a scientific computing course used ChatGPT for debugging, code generation, and concept explanation. While students appreciated the tool's assistance, the instructor observed that it led to reduced interaction during pair programming sessions, and in some cases, a drop in code quality. This suggests that easy access to GenAI may discourage collaboration and lead students to submit code they do not fully understand (Groothuijsen et al., 2024). Another study, by Kuramitsu et al. (2024) tested a model that automatically converted students' natural language descriptions into executable Python code. Although the tool was able to generate functional code for many of the student inputs, the authors cautioned that such convenience may result in students skipping the process of learning syntax, algorithms, and logic, core components of programming proficiency (Kuramitsu et al., 2024). A similar concern was raised by Haindl and Weinberger (2024), who studied undergraduate Java students using ChatGPT. While many students found the tool helpful for grasping theoretical concepts, they often hesitated to use its code suggestions in practice due to a lack of trust in the tool's accuracy (Haindl & Weinberger, 2024). These findings show that GenAI tools can lead to over-reliance, reduced collaboration with fellow students, and shallow learning.

#### 2.1.2 Student Engagement With GenAI

This section examines how students interact with GenAI tools in programming education, with a particular focus on individual learning strategies and skill development. Recent studies have investigated how students engage with GenAI tools in practice. The findings suggest that differences in self-regulation, conceptual understanding, and AI literacy may significantly shape students' ability to benefit from GenAI-supported learning.

One area of focus is how students engage with the tools. In a case study, Hartley et al. (2024) examined how undergraduate students used ChatGPT to support independent coding practice. While students found ChatGPT helpful for understanding syntax and clarifying errors, the study emphasized that its effectiveness was closely tied to the learner's self-regulation skills. Students who could plan their learning, formulate precise queries, and evaluate AI-generated responses were more successful. Those who didn't use these strategies often accepted incorrect or incomplete answers without reflection, suggesting that GenAI may widen the gap between more and less self-directed students (Hartley et al., 2024).

Jing et al. (2024) explored this further through a quasi-experimental design, investigating which factors most influenced students' effectiveness when using ChatGPT to solve programming problems. The study identified AI literacy, a student's understanding of how GenAI works and how to apply it critically, as a key predictor of effective use. Interestingly, students' intention to use the tool had no measurable effect on learning outcomes, while their knowledge of programming concepts and their knowledge of how ChatGPT operates had a significant impact. This highlights that using GenAI effectively requires more than technical skill, it depends on conceptual understanding and critical engagement with the tool itself (Jing et al., 2024).

Additional insights come from Phung et al. (2024), who compared the performance of GPT-3.5, GPT-4, and human tutors in various tutoring tasks. While GPT-4 was nearly on par with human tutors in explaining code and suggesting revisions, it struggled to perform more pedagogically complex tasks, such as tailoring feedback to student needs or designing new learning activities. This suggests that while GenAI can support procedural knowledge and provide surface-level feedback, it is less capable of fostering deep learning or adapting to a student's developmental level (Phung et al., 2023).

#### 2.1.3 New Competencies and Employer Demands

Several recent studies have examined how the growing use of GenAI in professional programming environments is shaping expectations for future employees. This section presents findings from recent research on how GenAI is being used in the workplace, the growing importance of AI literacy, and how academic programs might adapt to better prepare students for AI-integrated work environments.

A study by Clear et al. (2024) explored the implications of GenAI on professional roles through 47 interviews with IT professionals across New Zealand and Sweden. The findings revealed that GenAI is reshaping expectations in the industry, with professionals increasingly expected to engage with AI systems in tasks such as code generation, system design, and decision-making. AI tools are seen as augmenting human capabilities, requiring employees to combine traditional technical knowledge with higher-level skills like critical evaluation, ethical reasoning, and adaptability. The study emphasizes the need for educational institutions to evolve their curricula accordingly, ensuring that students not only learn how to use GenAI tools, but also how to navigate their implications within socio-technical systems (Clear et al., 2024).

A related shift is the growing emphasis on AI literacy. Stolpe and Hallström (2024) argue that preparing students for AI-integrated work environments requires more than teaching them how AI works; it requires helping them understand AI as a socio-technical phenomenon. Their proposed AI literacy framework includes not only technical knowledge and system thinking, but also ethical understanding and the ability to critically assess AI-generated content (Stolpe & Hallström, 2024). These insights align with findings from Jing et al. (2024), who showed that students with stronger knowledge of ChatGPT and a deeper understanding of its limitations, performed significantly better in programming tasks, reinforcing that AI literacy is central to effective participation in AI-enhanced workplaces (Jing et al., 2024).

Moreover, Abrahamsson et al. (2024) provided insights into how AI tools are used in real software engineering projects. Their study followed a graduate student team that developed a full-stack software platform using ChatGPT. While the project highlighted the tool's potential for automating tasks and improving productivity, it also underscored the importance of prompt engineering and human oversight in managing quality and coherence (Abrahamsson et al., 2024).

#### 2.1.4 Summary and Concluding Remarks

The reviewed literature offers insight into how GenAI is to influencing programming education. Across the three thematic areas, a number of key insights emerge.

First, studies suggest that GenAI tools can support learning when intentionally embedded in structured educational environments. Students report improved confidence, motivation, and understanding when AI is used as part of well-designed activities. However, several risks have also been identified. These include the potential for over-reliance on GenAI, reduced peer collaboration, and shallow engagement with fundamental programming skills.

Second, student outcomes vary considerably depending on their level of self-regulation and AI literacy. Research indicates that learners with strong metacognitive skills and conceptual understanding are better positioned to use GenAI effectively. This reinforces the idea that technical proficiency alone is not sufficient. Students must also critically evaluate AI-generated outputs and understand the limitations of these tools.

Third, GenAI is influencing expectations in the software industry, with employers placing increasing value on competencies such as AI literacy, ethical reasoning, and adaptability. As a result, programming education faces growing pressure to equip students not only with traditional technical skills but also with the ability to work effectively in AI-augmented environments.

Despite these valuable insights, the literature has some limitations. Many studies rely on small-scale classroom case-studies and self-reported data, and few examine long-term impacts. There is also a lack of cross-institutional and studies that could provide broader generalizability. Finally, while researchers have begun to outline the skills needed in an AI-integrated workplace, there is limited guidance on how educational institutions should adjust curricula and assessment to meet these needs.

---

## 3. Method

Kothari defines research methodology as the science of systematically studying how research is conducted, including the reasoning behind the choice of methods and their application to specific problems (Kothari, 2004). He emphasizes that methodology extends beyond the use of specific techniques, involving a deeper understanding of the assumptions underlying each method, the rationale for selecting one approach over another, and the limitations that follow. Adopting this broader perspective helps ensure that the research process is both logically structured and critically grounded.

In the field of information systems, Oates presents a clear and practical model of the research process in her book Researching Information Systems and Computing (Oates, 2006). Her model describes how research often begins with personal motivation and a review of existing literature, followed by the formulation of research questions, the development of a conceptual framework, and the selection of appropriate methodological strategies. It also highlights the importance of choosing suitable methods for data generation, such as interviews, questionnaires, or observations, along with a clearly defined analytical approach based on either qualitative, quantitative, or mixed methods (see fig. 3.1). Together, these frameworks inform the design of this study.

This chapter begins with an overview of the study's general design, and then provides detailed descriptions of each stage of data collection and analysis. The reasoning behind each methodological decision is made explicit to ensure transparency and alignment with the study's objectives.

### 3.1 General design of the study

Motivated by our own academic experiences with GenAI in education, the project began with a critical reflection on how these technologies were shaping our learning environment. To refine the scope and develop a relevant research strategy, a literature review was then conducted to map the current research landscape and identify gaps. The review revealed that existing studies are often based on small-scale case studies. To address these limitations and enable a broader and deeper understanding, a mixed methods design was developed, that combine multiple data sources. The design flow is visualized in fig. 3.2.

The composition of methods was selected to ensure a substantial exploration of the research questions from multiple perspectives. To begin with, our objective was to capture a wide range of perspectives on the use of GenAI in programming education. We initially considered standard research methods such as surveys, experiments, and interviews. However, we quickly identified significant limitations, particularly with survey-based approaches. The potential respondent pool would have been restricted primarily to NTNU students, limiting the diversity and scope of viewpoints. Additionally, the survey questions would likely have reflected our own prior experience and the specific themes addressed in the literature we had reviewed, thereby constraining the exploratory potential of the study.

After carefully evaluating available data sources capable of providing the breadth of perspectives we sought, we identified user comments on relevant, high-traffic YouTube videos as a valuable source of insight. This decision emerged during the project's initial exploratory phase, in which we actively sought international expert perspectives on the future of programming and GenAI. For instance, we were particularly interested in the views of key industry figures such as the CEOs of Nvidia and OpenAI. These perspectives are frequently expressed in recorded interviews, panel discussions, and keynote presentations published on YouTube, accompanied by extensive user engagement in the comment sections.

Ideally, the study would have included multiple YouTube videos and their associated comment sections to capture a broader spectrum of user perspectives. However, due to time constraints, the scope of a bachelor-level project, and the inclusion of additional research methods, the analysis was limited to a single video. At the time of data collection, the selected video had over 1,200 user comments. A custom Python script was used to extract and store the comments in a JSON file. The dataset was then analyzed using a combination of natural language processing tools, ChatGPT-4o, and manual thematic coding performed by the researchers.

Based on the analysis of user comments and a review of existing research, a set of targeted survey questions was developed to explore key issues that emerged from these earlier stages. Although a globally distributed survey targeting programming students across diverse educational settings would have been ideal, project constraints required a narrower focus. The finalized questions were therefore administered to third-year computer science students at NTNU, selected for their direct relevance to the institutional context and ease of access. With substantial academic experience and ongoing exposure to GenAI tools, this group was well positioned to reflect critically on how these technologies are shaping programming education. Survey results are presented in Chapter 4.

Building on the survey findings, we sought to enrich the empirical basis of the study through interviews with individuals directly engaged in both teaching and learning programming. This methodological extension was motivated by established research design principles, which emphasize the value of triangulating perspectives to capture the complex dynamics of educational change. Interviews were conducted with three instructors responsible for programming courses at NTNU and one first-year computer science student.

The primary emphasis was placed on instructors, due to their central role in shaping curricular responses to technological developments. Participants were selected based on prior knowledge of their engagement with GenAI and their varied approaches to its integration. Each had substantial experience in both academia and industry, contributing well-informed and differentiated views on the pedagogical, evaluative, and institutional implications of GenAI adoption.

The student interview complemented the survey data by offering a perspective shaped by early exposure to GenAI tools from the outset of formal programming education. In contrast to the third-year survey respondents, this student entered university after the widespread availability of GenAI tools, enabling comparative insights within the same institutional context.

Data from all sources, including YouTube comments, surveys and interviews, were analyzed in relation to one another. This integrative approach supported the identification of patterns, tensions, and points of convergence across public discourse, student experiences, and instructor perspectives, thereby deepening the overall understanding of how GenAI is reshaping programming education.

To summarize we followed the research methodology described in Oates, 2006 and formalized the following steps:

- **Experiences & Motivation.** Reflected on personal academic experiences and interests in programming education and GenAI to define a relevant problem domain.
- **Literature Review.** Conducted a literature review to map existing research, identify gaps, and inform both the research questions and the methodological design of the study.
- **YouTube Comments Analysis.** Collected and analyzed public comments on relevant videos to gain insight into global perspectives on GenAI in education.
- **Student Survey.** Designed and distributed a survey to third-year computer science students to capture experiences, usage patterns, and attitudes toward GenAI.
- **Interview Guide.** Developed a flexible set of key themes based on findings from previous stages to support unstructured interviews and guide open-ended, exploratory conversations.
- **Student Interview.** Conducted qualitative interviews with students to gain deeper insights into individual experiences and behaviors related to GenAI.
- **Expert Interviews.** Conducted interviews with experienced programming professors at NTNU to explore institutional perspectives and pedagogical approaches.

### 3.2 Literature Review

The literature review followed a systematic process, including the development of a structured search strategy, the application of predefined inclusion criteria, and the filtering and analysis of relevant studies through structured data extraction. This approach ensured methodological transparency and enabled a comprehensive overview of the existing knowledge base. Critically engaging with the literature allowed us to identify gaps, assess dominant methodological trends, and sharpen the focus of both our research questions and overall study design.

#### 3.2.1 Search Strategy

The search strategy was developed to align with the study's preliminary research objectives and to ensure comprehensive coverage of relevant literature. Keyword selection was informed by core concepts central to the study, and included both general and specific terms such as "artificial intelligence" and its common abbreviation "AI" to capture variation in terminology across publications. Boolean operators "AND" and "OR" were employed to combine terms and identify relevant intersections across thematic domains.

The final search query was iteratively refined and structured around four conceptual dimensions: (1) artificial intelligence, (2) education, (3) programming and computing disciplines, and (4) skills and competencies. The complete query was as follows:

```
("artificial intelligence" OR "AI") AND ("education" OR "curriculum"
OR "teaching" OR "learning" OR "teach" OR "learn" OR "school"
OR "university" OR "higher education") AND ("programming" OR "data
engineering" OR "software engineering" OR "programmers" OR "data
engineers" OR "software engineers" OR "computer science education")
AND ("skills" OR "competence" OR "knowledge" OR "capabilities"
OR "proficiency")
```

Searches were conducted in two major bibliographic databases, Scopus and Web of Science, selected for their comprehensive coverage of peer-reviewed literature in technology, computer science, and education (Clarivate, 2024; Elsevier, 2024).

#### 3.2.2 Inclusion Criteria

To ensure the quality and relevance of the literature included, a predefined set of inclusion and exclusion criteria was developed prior to the search process. These criteria were intended to guide the selection systematically and ensure alignment with the objectives and scope of the study. The complete criteria are presented in Table 3.1.

| Inclusion Criteria | Exclusion Criteria |
|---|---|
| Peer-reviewed publications | Non-peer-reviewed works (e.g., opinion pieces, preprints) |
| Published between 2023 and 2025 to ensure relevance post-ChatGPT emergence | Published before 2023 or after 2025 |
| English-language studies | Non-English articles |
| Addresses one or more of the predefined research areas | Focus unrelated to the defined research scope |

**Table 3.1:** Inclusion and Exclusion Criteria for Literature Selection.

#### 3.2.3 Article Filtering and Selection

To efficiently refine the pool of search results, the filtering process was carried out in two stages. In the first stage, predefined criteria were applied using database filters such as publication year, peer review status, subject area, and language. The resulting records were then screened by reviewing titles and abstracts to assess preliminary relevance.

In the second stage, we performed a full text review of the shortlisted to evaluate their methodological quality and substantive contribution to the research focus. This two-step process ensured that only high-quality studies offering meaningful insight into the defined research area were retained in the final selection.

As a result of the filtering process, a total of 18 high-quality articles were selected for inclusion in the literature review, presented in Table 3.2.

| Database | Subject Area | # in Subject | Total | Included |
|---|---|---|---|---|
| Scopus | Computer Science | 157 | 209 | 10 |
| | Engineering | 97 | | |
| | Social Sciences | 71 | | |
| | Mathematics | 22 | | |
| Web of Science | Computer Science | 113 | 223 | 8 |
| | Engineering | 85 | | |
| | Educational Research | 62 | | |
| | Science Technology | 17 | | |

**Table 3.2:** Comparison of search results across Scopus and Web of Science databases.

#### 3.2.4 Data Extraction and Analysis

Following the filtering process, we conducted a structured data extraction to systematically document and organize information from the remaining articles. For each article, we recorded the title, publication year, authors, research problem, methodology, main findings, relevance to our study, and noted limitations. This ensured that critical aspects of the literature were captured consistently. The extracted data was organized into a table to facilitate comparison and thematic grouping across studies.

### 3.3 Analysis of YouTube Comments

This section details the analytical procedures applied to explore user-generated discourse on GenAI in programming, based on comments extracted from a selected YouTube video. While the rationale for choosing this data source is outlined in Section 3.1, the present section offers a structured account of the analysis conducted, including justification for each methodological choice. Due to the scale, informality, and linguistic variability of the dataset, the approach was organized into multiple phases that integrate computational tools with researcher-led interpretation. The analytical workflow is illustrated in Figure 3.4.

1. Video selection
2. Data extraction
3. Thematic filtering using predefined keyword groups
4. Thematic exploration using ChatGPT-4o
5. Automated sentiment classification with pre-trained models
6. Researcher-led thematic and sentiment coding

This design was intended to combine analytical scalability with contextual sensitivity. Keyword-based filtering enabled efficient preprocessing by reducing the dataset to comments directly aligned with the research. ChatGPT-4o supported scalable thematic identification across large text batches while also capturing patterns beyond surface-level lexical cues. Automated sentiment classifiers provided breadth through rapid classification, whereas manual coding introduced a layer of interpretive depth by addressing nuances often missed by computational models. Together, these steps reflect a complementary design, where scalable tools ensure coverage and consistency, and human interpretation safeguards contextual relevance. Methodological constraints influencing these design choices are discussed in Section 3.3.1.

#### 3.3.1 Analytical Limitations and Design Considerations

The analytical framework was shaped by specific challenges inherent to YouTube comments, including informal language, sarcasm, fragmented phrasing, and frequent topic deviation (Bhimate et al., 2024). These features reduce semantic clarity and complicate both automated parsing and consistent human interpretation. To address these constraints, a mixed-method approach was adopted. Automated tools were employed to handle the volume and variability of the data, while manual coding provided necessary interpretive control. Each component of the framework introduced methodological limitations, requiring deliberate design choices to ensure coherence and reliability.

**ChatGPT for Thematic Exploration.** ChatGPT-4o (OpenAI, 2024) was applied to extract thematic patterns from the filtered comment dataset. The model enabled efficient synthesis across large text segments but presented methodological constraints. Its probabilistic output generation introduces variability across sessions and lacks full transparency, as outputs may reflect prompt phrasing rather than input content (Fiannaca et al., 2023; Turobov et al., 2024). This limits replicability and increases the risk of hallucinated or unsupported interpretations (OpenAI, 2023b). To reduce these risks, model outputs were manually reviewed. Extracted quotes were cross-checked against the source data, and themes without explicit textual support were excluded. Prompts were designed for clarity and specificity following established guidance (OpenAI, 2023a), and the dataset was divided into batches to prevent output degradation due to prompt length (Bommasani, Hudson et al., 2021).

**Sentiment Classification Models.** Three sentiment models VADER, TextBlob, and BERT were applied to enable comparative analysis. Each represents a distinct computational approach: VADER uses rule-based heuristics tailored to social media text, TextBlob applies polarity lexicons, and BERT leverages transformer-based language modeling trained on labeled reviews. While suitable for large-scale classification, these models face consistent challenges with ambiguity, irony, and context-sensitive expressions (Balahur & other authors, 2013; Rosenthal et al., 2017). A cross-model comparison showed low agreement, confirming limitations identified in previous studies and highlighting the difficulty of assigning sentiment labels in informal discourse (Hutto & Gilbert, 2014). To address these limitations, human-coded annotations were used to validate and adjust model outputs, improving alignment with the contextual meaning of the comments.

**Manual Coding Considerations.** Manual coding enables contextual interpretation but introduces subjectivity and scalability constraints. The accuracy of theme and sentiment labels depends on how consistently the coder applies the categories and how well they understand the context (Oates, 2006). To limit bias and improve reliability, a predefined coding framework was developed and used systematically (Section 3.3.6).

The following subsections describe each step of the analysis in detail.

#### 3.3.2 Video Selection

The selection was based on three predefined criteria, applied to identify a suitable source for user-generated commentary on GenAI in programming:

- **Content relevance:** The video had to explicitly discuss GenAI in the context of programming education or professional development.
- **Audience engagement:** A minimum threshold of 200,000 views and 500 comments was required to ensure a sufficiently diverse and engaged user base.
- **Timeframe:** The video had to be published within the past 24 months to reflect the current state of public discourse on GenAI.

Several videos were evaluated against the selection criteria to identify a source that combined thematic relevance, high engagement, and temporal currency. The video ultimately selected, titled "8 Rules for Learning to Code in 2025...and should you?", was published on December 19, 2023, by the YouTube channel Travis Media. The channel is operated by a self-described self-taught software developer and DevOps engineer who also maintains a blog and coding community for learners. This background supports the channel's credibility within its target audience and increases the likelihood that the comment section reflects authentic engagement from aspiring or active programmers.

At the time of data collection (April 18, 2024), the video had accumulated 512,000 views and 1,201 comments, thereby meeting the predefined thresholds for reach and interaction. These metrics indicate that the content had circulated widely and provoked substantial audience response, which is essential for a study aiming to analyze public discourse on GenAI in programming.

The video's content explicitly questions the future viability of programming careers in the age of generative AI and responds by emphasizing the continued relevance of foundational coding skills, deliberate practice, and technical adaptability. Framed around eight proposed rules for learning to code in 2025, the video combines motivational guidance with critique of premature reliance on AI tools. This thematic structure aligns closely with the study's research questions, which address learner motivation, evolving skill requirements, and perceptions of AI's role in programming education and employment.

#### 3.3.3 Data extraction

The comments were extracted using the open-source tool YouTube Comment Downloader (Bouman, 2022), which enables full retrieval of top-level comments without API restrictions. A total of 1,090 comments were successfully collected and saved in a structured CSV format for analysis.

#### 3.3.4 Thematic Filtering Using Keyword Groups

To focus the dataset on comments relevant to the study's objectives, it was filtered using regular expressions grouped into three thematic categories:

- **Programming Education:** `learn(ing)?, teach(ing)?, educat(ion|ional)?, student(s)?, class(room)?, course(s)?`
- **Generative AI:** `\bai\b, artificial intelligence, genai, chatgpt, llm, gpt-4, copilot`
- **Developer Industry:** `developer(s)?, programmer(s)?, software engineer(s)?, job(s)?, career(s)?, tech, workplace?, industry, hire(d|ng)?, recruit(ment)?`

Comments containing at least one of the specified expressions were retained, reducing the dataset to 622 comments (57% retention rate).

Each group corresponded to the following research questions:

- Programming Education → RQ1 and RQ2
- Developer Industry → RQ3
- Generative AI → All RQs

This approach increased thematic precision but risked excluding comments with relevant content expressed outside the targeted vocabulary. This trade-off was accepted to ensure analytical coherence and reproducibility.

#### 3.3.5 Thematic exploration with ChatGPT-4o

ChatGPT-4o (OpenAI, 2024) was used to extract recurring themes from the dataset, as it allows large-scale text analysis while preserving contextual meaning. This made it possible to identify thematically relevant content that would not be detected through keyword filtering alone. Each batch of comments was submitted with a standardized prompt, and the model's outputs were manually reviewed to ensure thematic relevance and consistency with the research questions.

**Batching and Prompt Design.** To manage the limitations associated with large prompt inputs discussed in Section 3.3.1 the dataset was divided into 13 batches: 12 containing 50 comments each, and a final batch with the remaining 21 comments. Each batch was formatted as a numbered list and submitted as plain text in the prompt window to maximize clarity and minimize ambiguity (OpenAI, 2023a). A uniform prompt was used across all batches, instructing the model to identify up to five central themes, each accompanied by a brief explanation and direct quotes from the input. The inclusion of quotes enabled transparent validation against the original dataset and allowed for assessment of how ChatGPT-4o interpreted the source material. The prompt followed established prompt engineering principles, including precise task definition, clarity of instruction, and grounding in source content, in line with OpenAI's best practices (OpenAI, 2023a):

> You are a research assistant helping to identify recurring themes in a dataset of public comments. Based solely on the comments provided, extract up to five central themes relevant to GenAI in programming education or software development. For each theme, provide a brief explanation and include direct quotes as evidence. Do not speculate or generate content not found in the comments.

**Verification and Quality Control.** To ensure analytical rigor, the following review process was implemented:

- A subset of outputs from each batch was carefully reviewed.
- Suggested quotes were cross-checked against the input text to verify authenticity.
- The relevance and consistency of each proposed theme were evaluated based on the supporting comments.
- Themes judged to be vague, overly general, or unsupported by quotes were either revised or excluded.

No fabricated content was identified in the reviewed outputs, and all included themes were grounded in the original comment data set.

**Thematic consolidation.** After completing the batch-level analysis, all identified themes (n = 65) were compiled into a single dataset. This set was then submitted to ChatGPT-4o with a separate consolidation prompt, designed to group conceptually similar themes into broader, overarching categories. Unlike the batch prompt, this consolidation prompt imposed no limit on the number of categories or sub-themes, allowing for open-ended synthesis across the full dataset. ChatGPT-4o generated seven overarching thematic categories. Each of the 65 batch-level themes was manually reviewed and assigned to one category if a clear match was evident, based on the theme label, explanation, and supporting quotes. Themes that were ambiguous or did not clearly align with any grouping were left uncategorized but considered in the qualitative interpretation. The final categorization yielded the following seven overarching thematic categories:

1. AI as a Tool, Not a Replacement
2. Job Market Uncertainty
3. Overreliance and Foundational Skills
4. Passion and Motivation to Learn
5. Limitations of AI / Human Oversight
6. Ethics and Ownership
7. Generational Shifts / Resistance vs. Embrace

The distribution of the 65 identified themes across the 13 analyzed batches, as well as the overarching thematic categories used in the analysis, are presented in section 4.1.2 in Results.

#### 3.3.6 Sentiment Classification

This section details the procedure used to assign sentiment labels to filtered YouTube comments. A dual approach was adopted to balance scale and interpretive accuracy: pre-trained sentiment models enabled large-scale classification, while human-led coding ensured contextual validity. The combination was selected to compensate for known weaknesses in each method and allow for cross-validation of results.

**Automated Sentiment Classification.** Three sentiment models were applied, each representing a distinct computational approach:

- **VADER (Hutto & Gilbert, 2014):** A rule-based model optimized for social media text. It calculates a compound sentiment score ranging from -1 to 1, where comments are labeled as positive if compound >= 0.05, negative if compound <= -0.05, and neutral otherwise.
- **TextBlob (Loria, 2018):** A lexicon-based model that computes a polarity score in the interval [-1, 1]. Sentiment labels are assigned as positive for scores > 0.1, negative for scores < -0.1, and neutral in between.
- **BERT (Town, 2020):** A transformer-based model trained on product reviews to predict star ratings from 1 to 5. These ratings were mapped to sentiment labels as follows: 1-2 stars = negative, 3 stars = neutral, 4-5 stars = positive.

Labeling thresholds are summarized in Table 3.3. Despite established heuristics, the models produced inconsistent results. 26.6% of comments received matching sentiment labels across all three, and agreement between VADER and BERT occurred in 47.2% of cases. These inconsistencies reflect prior findings that rule- and lexicon-based models struggle with sarcasm, ambiguity, and context-dependence (Balahur & other authors, 2013; Rosenthal et al., 2017). Automated outputs were not treated as definitive but served as a scalable baseline for comparison.

| Model | Sentiment Labeling Rule |
|---|---|
| VADER | Compound score >= 0.05: positive, <= -0.05: negative, else: neutral |
| TextBlob | Polarity > 0.1: positive, < -0.1: negative, else: neutral |
| BERT | Stars 4-5: positive, 3: neutral, 1-2: negative |

**Table 3.3:** Heuristics used to assign sentiment labels from each model.

**Human-Led Sentiment Coding.** To gain deeper insight into public sentiment and to evaluate the reliability of model-generated classifications, a subset of 90 comments was manually annotated by the researchers. Each comment was assigned a sentiment label based on a predefined classification framework designed to capture evaluative stances regarding the impact of generative AI on programming and the role of developers.

- **Positive:** Comments that express optimism, enthusiasm, or confidence about the impact of generative AI on programming or the future of developers. This includes support for AI as a learning or productivity tool, endorsement of human-AI collaboration, or beliefs that AI will enhance rather than replace developer roles.
- **Negative:** Comments that express concern, skepticism, or criticism about the consequences of generative AI in programming. These include fears of job loss, the decline of foundational coding skills, over-dependence on automation, or doubts about the reliability or usefulness of AI-generated code.
- **Neutral:** Comments that are descriptive, informational, or speculative without conveying a clear positive or negative sentiment. These may report observations, share experiences, or discuss concepts without endorsing or criticizing AI's role or consequences.
- **Mixed:** Comments that combine both positive and negative views on generative AI's impact. These often highlight potential benefits while acknowledging risks, tensions, or limitations. This label was used when the comment presented a balance of perspectives or when no single sentiment clearly dominated.

Example classification:

> "AI is not creative like humans."

This comment was classified as Mixed. While it critiques AI by stating a limitation (lack of creativity), it also implicitly affirms the unique value of human abilities. This suggests continued reliance on human developers and indirectly supports the idea that AI will not fully replace them. Because it highlights a limitation of AI in a way that favors human relevance, it reflects both skepticism and reassurance, fitting the "mixed" category under this framework. This interpretive layer enabled context-sensitive evaluation of sentiment and supported comparative validation of the automated models.

During this process, the recurring claim "coding is dead" stood out as particularly relevant. Comments affirming the phrase were labeled negative, often reflecting concerns about obsolescence. In contrast, comments that rejected the claim arguing that programming is evolving or remains essential were labeled positive, framing GenAI as a complement rather than a replacement.

**Model Comparison.** The 90 manually labeled comments were compared against the sentiment classifications generated by all three models. Agreement with human labels was as follows: VADER (35.6%), BERT (31.1%), TextBlob (28.9%). Majority vote matched the manual label in 33.3% of cases. In 8 instances, all models disagreed with each other and the human label. These findings support the decision to use hybrid sentiment analysis. Hybrid coding strengthens validity and interpretability. The combination allows for scalable analysis without compromising analytical depth.

### 3.4 Survey

To systematically collect quantitative data on students' experiences with and attitudes toward GenAI in programming education, a survey was developed and distributed. The survey targeted third-year computer science students at NTNU. This group was selected due to their extensive exposure to programming courses across several semesters, and their experiences before and after the emergence of GenAI tools like ChatGPT and GitHub Copilot.

The survey was primarily designed based on insights from the literature review, with inspiration drawn from recurring discussion patterns observed during the YouTube comment analysis. It consisted primarily of multiple-choice and Likert scale questions, covering the themes: usage patterns of GenAI tools and perceived impact on learning and programming skill development.

The survey was constructed using University of Oslo's digital survey tool (Nettskjema) and was distributed internally to the students through NTNU communication channels. Participation was anonymous and voluntary, and the survey was designed to take approximately two minutes to complete, encouraging a high response rate.

### 3.5 Constructing The Interview Guide

Two separate unstructured interview guides were developed, one for the expert interviews and one for the student interview. The guide outlined key themes to be addressed during the conversations. These themes were derived from earlier stages of the research process, including the literature review, YouTube comment analysis, and the student survey (see Figure 3.2). The purpose of the guide was to ensure relevance to the research questions while allowing flexibility to follow individual lines of reasoning and for the emergence of new insights.

Unstructured interviews are flexible, open-ended conversations where the interviewer does not follow a fixed set of questions. Instead, questions are adapted in response to the participant's input, allowing the interviewer to explore emerging themes or skip irrelevant topics (Kothari, 2004). This format is especially useful in exploratory research, as it enables deeper insights into personal experiences and motivations. However, it also requires more skill from the interviewer and can be harder to analyze due to the varied nature of the responses.

#### 3.5.1 Expert Interviews (Process)

Three expert interviews were conducted with programming instructors at NTNU to gather insight into how GenAI is perceived within teaching practice. Each interview was scheduled for one hour and conducted in person. One researcher led the conversation, while the other took notes and contributed follow-up questions. This division of roles enabled both consistent structure and active engagement. The interviews followed a conversational format, with participants encouraged to share reflections and experiences freely, and the researchers adapting their questions in response to the direction of the discussion.

After each interview, the notes were reviewed and rewritten. Key points were identified, and the material was organized thematically to reflect recurring areas of focus. This post-interview structuring made it possible to trace patterns across the conversations while preserving the individual character of each expert's contributions.

#### 3.5.2 Student Interview (Process)

In addition to the expert interviews, a single unstructured interview was conducted with a first-year computer science student at NTNU. The student was purposefully selected based on prior knowledge of their interest in GenAI in education, and because they had no programming experience prior to beginning their studies. This made the participant well suited to offer insight into how early exposure to GenAI might influence learning strategies, confidence, and motivation.

The interview followed the same unstructured format and thematic framework as the expert interviews, guided by a separate student-specific interview guide. As with the expert interviews, one researcher led the conversation while the other took notes and contributed when relevant. The conversation was open and exploratory, allowing the student to describe their own experiences and perspectives freely.

After the interview, the notes were reviewed and rewritten to highlight key insights. The responses were then thematically structured to allow comparison with findings from the other data sources.

---

## 4. Results

This chapter presents the main findings of the study, based on the data collected through multiple methods. The results are organized by data source, beginning with insights from YouTube comment analysis, followed by the student survey and the interviews with three experts and the student. Each section highlights relevant themes and patterns that address the research questions.

### 4.1 YouTube Comment Analysis

This section presents the findings from the analysis of comments posted under the YouTube video "8 Rules for Learning to Code in 2025...and should you?" reflected on in Section 3.3.2. The results are organized according to the analytical phases outlined in Section 3.3.

#### 4.1.1 Filtering by keywords

The keyword-based filtering procedure reduced the dataset from 1,090 to 622 comments, yielding a retention rate of 57.1%. Each retained comment matched at least one of the predefined thematic groups:

- Programming Education: 252 comments (40.5%)
- Generative AI: 326 comments (52.4%)
- Developer Industry: 357 comments (57.4%)

The distribution of comments across thematic categories reveals substantial thematic overlap, as illustrated in Figure 4.1, where circle size reflects the number of comments. The visualization shows that many comments engage with multiple dimensions of the research framework. Notably, 51 comments address all three thematic areas: Programming Education, Generative AI, and Developer Industry, while substantial overlap also exists between pairs of categories, such as Generative AI and Developer Industry (94 comments) and Programming Education and Developer Industry (59 comments).

Figure 4.2 presents the frequency of keyword matches across the three thematic groups. In the Programming Education category, learn / learning appears most frequently, with 220 matches, indicating that learning-related terminology is a central component of this group. The Generative AI group is dominated by the general term AI (317 matches), while more specific terms such as LLM, Copilot, and ChatGPT occur far less often. Within the Developer Industry group, the most frequently matched keywords are work / workplace (150) and job(s) (136), followed by developer(s) (72) and tech (59). These frequencies reflect how the thematic categorization is distributed across commonly used terms and suggest that the comments retained for analysis include a substantial concentration of discourse related to learning, artificial intelligence, and employment contexts.

#### 4.1.2 Thematic patterns identified by Chat-GPT

A total of 65 unique themes were identified across 13 batches of YouTube comments and subsequently grouped into seven overarching thematic categories, as outlined in the methodological approach in Section 3.3.5. The categories are presented below in descending order based on the number of batches in which they appeared, beginning with the most frequently observed. This structure highlights which thematic concerns were most prominent in the dataset.

**1. Job Market Uncertainty.** Themes related to job displacement, employment risk, and changing career prospects were identified in 10 out of 13 batches. Examples include: Job Displacement and Role Evolution in Software Engineering; Job Market Friction: Interviews, Hiring Practices, and AI's Impact; Job Market Uncertainty and Displacement Fears; Career Uncertainty and Motivation; AI Anxiety and Job Market Uncertainty.

**2. Limitations of AI / Human Oversight.** Themes emphasizing the limitations of AI systems or the continued need for human input were present in 9 batches. These included references to abstract reasoning, creativity, critical thinking, and oversight. Representative examples: The Irreplaceable Role of Human Abstraction and Design; AI Still Has Limitations and Requires Human Oversight; Human Skills Still Matter — Especially Knowledge, Creativity, and Oversight; Limitations of AI in Complex Software Development.

**3. Generational shifts / Resistance vs. Embrace.** This category appeared in 8 batches, capturing themes that point to a broader shift in how software development is practiced and perceived in the context of generative AI. Several themes highlighted tensions between established norms and emerging expectations, as well as the evolving nature of skills required in the field.

**4. AI as a Tool, Not a Replacement.** This framing was explicitly present in 7 batches, with commenters describing AI as a supportive rather than substitutive technology.

**5. Passion and Motivation to Learn.** This theme also appeared in 7 batches, with comments discussing motivation, intrinsic interest, and emotional engagement with programming in the context of AI.

**6. Over-reliance and Foundational Skills.** This category was represented in 5 batches. Themes highlighted concerns that reliance on AI might undermine core competencies.

**7. Ethics and Ownership.** This theme was present in 1 batch, specifically: Ethical and Ownership Concerns with AI Tools.

#### 4.1.3 Sentiment Classification Results

This section presents the results of the sentiment analysis conducted on the YouTube comments, following the dual-method approach outlined in Section 3.3.6.

**Model Sentiment Distribution.** Figure 4.3 displays the sentiment distribution produced by each of the three models. VADER classified 62.6% of comments as positive, 14.9% as neutral, and 22.5% as negative. TextBlob assigned 51.5% to the positive category, 41.3% as neutral, and 7.1% as negative. BERT labeled 38.4% of comments as positive, 20.9% as neutral, and 40.7% as negative.

**Model Agreement.** Out of the 622 comments analyzed, all three models assigned the same sentiment label for 164 comments (26.4%), while VADER and BERT agreed on 293 comments (47.1%). These agreement rates reflect variation in how the models interpret sentiment categories. Differences in underlying methodologies may influence which aspects of the text each model prioritizes when assigning a label.

| Sentiment | VADER | TextBlob | BERT |
|---|---|---|---|
| Positive | 62.6% | 41.3% | 38.4% |
| Neutral | 15.0% | 41.3% | 20.9% |
| Negative | 22.7% | 7.1% | 41.0% |

**Table 4.4:** Sentiment model results for n = 622.

#### 4.1.4 Distribution of manual Sentiment labeling

Among the 90 comments manually coded by the researchers, the overall sentiment leaned toward a positive outlook. Specifically, 36 comments (40%) were categorized as positive, followed by 26 as negative (28.9%), 20 as neutral (22.2%), and 8 as mixed (7.8%). This distribution reflects a generally optimistic tone, although concerns and ambiguities were also present.

Positive comments frequently highlighted perceived benefits of generative AI, particularly its role in enhancing productivity, supporting learning, or complementing human developers. For example, one user stated: "AI is useful for beginners... it makes so much easier to understand things", indicating enthusiasm for AI as an educational tool. Notably, several comments directly countered the recurring phrase "coding is dead", affirming instead that programming is evolving, not disappearing. These were classified as positive because they positioned AI as a complement rather than a threat, reinforcing developer relevance.

In contrast, negative sentiments often reflected concerns about job displacement, skill degradation, or excessive reliance on automation. A representative comment warned: "Coding with AI without learning how to code... it will all come crushing down", reflecting anxiety about foundational knowledge being eroded.

Comments classified as mixed acknowledged both benefits and risks, often emphasizing trade-offs. For instance, "It'll be a true friend for the few developers who will still have jobs" simultaneously praised AI's utility while expressing concern over employment.

Neutral comments typically conveyed factual or descriptive statements without clear emotional valence. These included reflections on personal learning journeys or questions about domain specialization, such as: "No the question is what domain or ecosystem should I focus on which should be guided by your interests."

Among the 90 manually labeled comments, 11 explicitly referenced the phrase "coding is dead". Of these, six were labeled as positive, four as negative, and one as neutral. The negative comments typically associated the phrase with concerns about job loss or the automation of programming tasks by AI. In contrast, the positive comments rejected the claim, describing programming as an evolving discipline and emphasizing continued relevance of human roles such as system design and oversight. This distribution illustrates divergent interpretations of GenAI's impact on programming and highlights variation in how the concept of obsolescence is addressed in public discourse.

#### 4.1.5 Model Agreement with Manual Coding

Table 4.5 summarizes the level of agreement between the human-coded sentiment and the predictions of the three sentiment models. VADER showed the highest agreement rate (35.6%), followed by BERT (31.1%) and TextBlob (26.7%). In 11 cases (12.2%), all three models agreed with the manual label. These findings suggest moderate alignment but highlight important differences across models.

| Model | Agreement with Manual |
|---|---|
| VADER | 32 (35.6%) |
| TextBlob | 24 (26.7%) |
| BERT | 28 (31.1%) |
| All models agree | 11 (12.2%) |

**Table 4.5:** Agreement between sentiment models and human-coded labels for 90 comments.

### 4.2 Student Survey Results

This section presents the results from the survey sent to 96 third-year computer science students at NTNU. A total of 43 responses were collected. The figures below display the findings of each question, accompanied by short interpretations.

**Reliance on GenAI for coding tasks.** The first survey question asked students how much they rely on GenAI tools, when working on programming tasks. Responses were given on a scale from 0 (not at all) to 5 (very much). As shown in Figure 4.5, most students reported moderate to high reliance on GenAI. Almost half of the respondents (46.5%) selected level 3 and more than a quarter (27.9%) selected level 4. No respondent indicated no reliance at all. These results indicate that GenAI tools have become a common part of students' everyday programming practices.

**Usefulness of GenAI for Becoming a Better Programmer.** As shown in Figure 4.6, most students perceived AI tools as beneficial or somewhat beneficial to their programming skills. A total of 41.9% agreed that AI enhances their skills and understanding, while 44.2% expressed mixed feelings, acknowledging concerns about over-reliance. 11.6% stated that they do not feel AI has helped them improve due to dependency issues. The responses indicate that although students recognize the usefulness of GenAI tools, many also express concerns about reliance.

**Impact of GenAI on the Perceived Value of Lectures.** Figure 4.7 shows that 34.9% of students reported attending fewer lectures, as GenAI tools could answer many of their questions more efficiently. However, 30.2% still viewed lectures as important for achieving deeper understanding. Another 27.9% said GenAI had not affected their opinion of lectures, while 7.0% said they already did not attend lectures. These results indicate that GenAI may be reshaping learning habits, but lectures remain valuable to many students.

**Changes in Programming Confidence Due to GenAI.** As shown in Figure 4.8, student responses were mixed. While 23.3% felt more confident with GenAI support, a larger share (34.9%) reported feeling less confident and more dependent on the tools. 27.9% felt that their confidence level had not changed. These findings highlight that students engage with GenAI in diverse ways, leading to different outcomes in terms of self-confidence.

**Negative Effects of Using GenAI for learning.** As shown in Figure 4.9, the most common concerns were: 27 participants reported that they spent less time thinking through problems, 24 stated that they relied too much on AI and found it harder to code from scratch, and 21 reported copying code without fully understanding it. These findings highlight the potential trade-offs of GenAI use in learning, particularly in relation to long-term skill development.

**Perceptions of Coding's Future Relevance.** As shown in Figure 4.10 a majority foresee a shift toward AI-assisted development. While some maintain that traditional coding will remain essential, others anticipate a future where traditional coding may be replaced.

**Preferred Source of Help: AI vs. Human Support.** As shown in Figure 4.11, a majority of students reported turning to AI tools first when they need help. Only a few participants chose teaching assistants or professors as their preferred help. This shift indicates that GenAI has become a primary preferred source of help.

**Usefulness of TA Sessions.** As shown in Figure 4.12, a minority still find TA sessions equally useful as before, a significant portion rely on GenAI to address simpler problems, using TA support more selectively. Others report replacing TA sessions entirely with GenAI tools.

### 4.3 Expert Interview Results

The following section presents findings from three expert interviews conducted with professors at NTNU. Each interview lasted one hour and was conducted in Norwegian. For anonymity, the professors are referred to as Expert 1, Expert 2, and Expert 3.

#### 4.3.1 Interview with Expert 1

**Background:** Expert 1 teaches a large introductory programming course at NTNU. He has a broad interest in the role of AI in programming and learning. His reflections center on foundational learning and educational responsibility.

**AI and the Learning Process.** Expert 1 emphasizes that learning programming is not just about achieving results but about going through the mental process of problem-solving. He compared the learning journey to a graph where knowledge is zero at the origin, and real learning occurs during the "ups and downs" of failure and correction. He expressed concern that large language models offer students a shortcut to solutions without real understanding, weakening the learning process. He believes that while students with strong fundamentals can benefit from AI tools, beginners with little prior knowledge are unlikely to gain meaningful understanding. "It gives the illusion of learning without the actual struggle," he noted.

**Programming Education Philosophy.** In his view, programming courses should help students develop curiosity and domain-oriented thinking. He focuses on creating engaging exercises and learning sessions that make students want to learn more. However, after the pandemic, he has seen a major decline in lecture attendance. He attributes this to a lack of perceived value from students who see AI as a convenient shortcut. He believes educators must show students the long-term value of deep understanding.

**Assessment.** He supports using traditional written exams rather than take-home assessments, since it is harder to cheat. However, he is skeptical of using exam grades to evaluate the effects of GenAI's impact on students, due to the varying difficulty of exams, grading, and teaching styles. He also warns that making exams harder could unintentionally encourage students to rely more on powerful AI tools to keep up.

**Role of AI in Development.** Although he acknowledges AI's strengths, he remains doubtful of its ability to contribute meaningfully at the architectural or systems level. In his words, "AI doesn't have the tacit knowledge that comes from hallway conversations or understanding what a client really wants". He also argues that AI lacks real understanding and innovation. "AI is not creative, it just reproduces what we've already done statistically". Thus, he does not see it as a replacement for skilled human developers.

**Personal and Societal Reflections.** Expert 1 reflected on his own experience during the dot-com bubble, when fears of obsolescence were widespread. He believes we are witnessing a similar overreaction to AI today, with hype fueled by investors and tech leaders. He is particularly concerned about how this affects young students: "We risk raising a generation that stops thinking because they expect instant answers". He believes that students should still learn fundamentals, possibly including syntax, and he cautions against abandoning foundational skills.

**Qualities in Students.** He argues that passion, curiosity, and mental engagement are far more important than raw technical skill. Students who genuinely want to learn and understand will adapt over time. Those who rely solely on AI tools without this mindset will struggle in the workforce.

**Broader Educational Challenge.** Finally, he poses a deep pedagogical question: At what abstraction level should we begin teaching programming in the age of AI? While he doesn't have a definitive answer, he leans toward preserving low-level understanding as a foundation, even if some practical tasks are automated.

#### 4.3.2 Interview with Expert 2

**Background:** Expert 2 teaches both introductory and advanced programming courses at NTNU. He has a research background in software engineering and how AI impacts both industry and education. His approach emphasizes critical thinking, abstraction, and preparing students for the real-world challenges of modern software development.

**AI as a Tool, Not a Crutch.** Expert 2 underlined that responsibility for the use of AI ultimately lies with the user. AI can be a helpful assistant, much like a human colleague, but one must critically assess its output. "Just like humans, AI can be wrong," he noted. Therefore, students must be trained to think critically about when and how to trust AI-generated results. He emphasized that AI tools are especially helpful in some areas, like generating documentation or solving small coding tasks, but far less effective when dealing with complex problems that require deeper understanding or systemic thinking.

**Adapting Education to Reflect Industrial Change.** In his view, programming education should shift to better reflect what students will face in industry. Rather than drilling syntax or language-specific tricks, teaching should focus on higher-level skills: understanding code logic, evaluating correctness, and solving problems abstractly. He sees a parallel between past transitions (from machine code to modern programming languages) and the shift AI is now bringing. In both cases, the baseline of abstraction is rising. "We used to teach machine language, now we don't need that anymore. AI will push that boundary further."

**Changing the Role of Lectures.** Expert 2 acknowledged that fewer students now attend lectures, and he sees this as a challenge. He believes programming is fundamentally a practical skill, and that education should include less passive theory and more hands-on labs. "Understanding grows through doing," he argued. Despite this, he has not seen a dramatic decline in attendance in his own courses, especially in more advanced classes. He believes students will still show up when they see clear value in what's being taught, especially material that can't be easily found online or outsourced to AI.

**Limits of AI for Novice Learners.** He expressed concern that beginners are more at risk when using AI tools. If a student lacks basic understanding, they are more vulnerable to so-called "hallucinations" from language models, where the AI produces false or misleading content. He believes students need to be made aware of these risks. "You only benefit from AI if you already understand the topic. Otherwise, you're just copying something you don't know is wrong."

**Role of Syntax in the Future.** Expert 2 believes that learning syntax is becoming less critical. Instead, students should focus on understanding how to interpret and reason about code. Reading and verifying code is more important than memorizing how to write it, especially with tools like Copilot or ChatGPT assisting with boilerplate code. However, he does not believe we can yet fully eliminate low-level knowledge. Students still need to understand how the system works to use AI tools effectively.

**Ethical Uncertainty.** He noted growing uncertainty among students about what constitutes cheating. Many students are unsure if using AI tools like ChatGPT is allowed. He emphasized the importance of clear institutional guidelines and increased awareness about how and when to use these tools responsibly.

**Future of Programming and the Role of Developers.** When asked whether AI will replace developers, he was optimistic. "I think the opposite will happen," he said. Developers will be freed from lower-level tasks, allowing them to focus more on creative and complex challenges. He does not believe that everyone will become a programmer, but he sees programming as a basic digital literacy skill, much like reading or writing. He warned, however, that gaps may grow between those who adapt and those who don't. He specifically mentioned countries or regions that fail to introduce programming and digital tools early in education as being at risk of falling behind. Rather than emphasizing specific languages or frameworks, Expert 2 argued that future developers need to be problem-solvers. Skills like algorithmic thinking, contextual awareness, and adaptability will be most important.

#### 4.3.3 Interview with Expert 3

**Background:** Expert 3 teaches programming courses at NTNU and actively integrates AI tools into his teaching. With long-standing industry and academic experience, he draws a sharp distinction between simply writing code and being a true software developer. His teaching philosophy emphasizes system understanding, critical thinking, code quality, and active student engagement.

**Programmer vs. Developer.** Expert 3 emphasized a crucial distinction: knowing how to write code does not make you a developer. A developer must understand systems holistically, how components interact, how to design architecture, and how to deliver maintainable software. This perspective shapes his view on AI: tools like Copilot can assist with writing code, but they do not replace the judgment and architectural thinking of a skilled developer.

**Teaching Approach and Use of AI.** Expert 3 actively incorporates GitHub Copilot and ChatGPT into his teaching, not just to demonstrate their capabilities but to foster critical evaluation of their outputs. In lectures, he often begins by showing how easily Copilot can generate code from a simple comment, illustrating the efficiency these tools offer. However, he uses this as a pedagogical entry point. To emphasize the importance of quality and robustness, he takes the code suggested by Copilot and pastes it into ChatGPT, asking what could be improved or made more resilient. This practice helps students see that even though AI-generated code can appear correct, it often lacks proper error handling, input validation, or structural clarity. By comparing and critiquing these outputs in real time, students are encouraged to reflect on what makes code not just functional, but reliable and maintainable. He requires students to document their use of AI tools in their exam assignments, thereby promoting transparency and awareness about tool dependency.

**Code Quality.** Expert 3 emphasizes code quality concepts like cohesion, coupling, and design patterns. He believes students should be trained to evaluate whether code is well-structured and maintainable.

**The Role of AI in Development.** He partially agrees with the phrase "coding is dead," in the sense that many people can now generate code, but that doesn't mean everyone can build good software. What separates a developer from a code generator is the ability to understand the higher abstraction level and shape systems. In his courses, he shows how Copilot can automate routine tasks, but always under the assumption that the student understands what's being built, and critically evaluate the output.

**Active Learning and Class Design.** He critiques passive learning, especially the traditional "slides-and-lecturing" model. "You don't become a good programmer by watching someone else solve problems," he said. Instead, his classes are structured around doing. Using a top-down approach, he first demonstrates larger structures, like how classes and objects work, before digging into the details. He uses tools like BlueJ to visually connect code to concepts, helping students understand program structure before introducing the syntax. His classes are highly participatory: he live-codes together with students, pauses frequently to invite input, and encourages collaborative problem-solving throughout the lecture. He notes that attendance in his sessions is the same as before GenAI tools became widely available.

**AI in Education.** He sees great value in AI as a pedagogical tool if used thoughtfully and aligned with clear learning objectives. It should foster critical thinking and reflection. Simply copying AI-generated code misses the point. Instead, teachers should design exercises that ask students to analyze, evaluate, or justify their use of AI, skills that go beyond replication.

**AI and the Future of Programming.** Reflecting on his own early career, he noted that he once used a system that auto-generated C code from defined system states. The fact that we're still manually writing syntax today, 30 years later, feels regressive to him. He believes AI should free us from repetitive tasks and allow us to focus on higher-order thinking.

### 4.4 Student Interview Result

**Background:** The student participant, referred to here as Student A, is currently enrolled in a bachelor's program in software engineering. She began her degree after the release of ChatGPT and has had continuous access to generative AI throughout her education. Her reflections provide a first-hand perspective on how students are navigating programming education in parallel with the rise of GenAI.

**Perceived Benefits of ChatGPT.** Student A expressed that ChatGPT made her feel more motivated, largely because it allowed her to work faster and more efficiently. She described the tool as an accessible and judgment-free personal tutor, particularly helpful for asking questions she might otherwise avoid in class. She emphasized that ChatGPT explains things clearly and in a simplified manner, making it easier to understand difficult concepts in programming.

**Concerns About Learning Depth.** She was also aware of the potential downsides. She believed that she had likely learned less by using ChatGPT than she would have without it, especially because she did not struggle through problems to the same degree. "You learn by struggling" she said, and when AI delivers ready-made answers, that process is interrupted. She also mentioned that fully understanding the topic can be challenging, and that when she uses AI tools, the knowledge she gains doesn't always "stick".

**Attitudes Toward Lectures.** Student A noted that programming lectures were often difficult to follow, especially when topics became advanced or lacked structure. In these situations, turning to AI tools felt like a more productive learning strategy. However, she also stressed that a good lecturer can reduce the need for AI assistance. When instructors are engaging, motivating, and able to clearly connect the broader picture, students are more likely to remain in the classroom and rely less on external tools.

**Hybrid Learning.** Looking forward, she suggested a hybrid educational model. In her view, human teachers should act as motivators, framing the subject, creating interest, and showing how the pieces fit together. In parallel, AI tools could serve as personalized assistants that explain material in detail and adapt to individual learning needs. She believed this combination could help students achieve both engagement and deeper understanding.

---

## 5. Discussion

This chapter discusses the findings in relation to the three research questions guiding the study. It also reflects on the methodological limitations, and future research.

### 5.1 Interpretation of Key Findings

**RQ1: How has the emergence of generative AI impacted programming education?**

The emergence of GenAI has had a noticeable impact on programming education, as reflected in the findings of this study. Survey data show that students tend to prefer GenAI tools over seeking help from teaching assistants or educators when they encounter programming challenges. Some students also report skipping lectures in favor of relying on AI assistance. Thematic analysis of YouTube comments highlights that learners commonly use AI as a learning and coding assistant, and as a productivity tool.

The first year student interviewed in the study described ChatGPT as a helpful and judgment-free tutor that improved her motivation by allowing her to work more efficiently. Among the experts interviewed, one points out a decline in lecture attendance, attributing it partly to students viewing AI as a shortcut to learning. He emphasized the need for educators to better communicate the long-term value of deep understanding. Another expert compared the current shift to AI with earlier shifts in programming education, such as moving away from machine code to higher level languages, arguing that AI is raising the level of abstraction. The third expert has not observed any change in attendance or engagement in his own lectures. He has adapted his teaching format by incorporating tools like ChatGPT and GitHub Copilot into his lectures, using live coding and encouraging student engagement throughout the sessions.

**RQ2: What are the positive and negative effects of using generative AI in programming education?**

The results of this study suggest that the use of GenAI in programming education has both positive and negative effects. Sentiment analysis of YouTube comments revealed a balanced mix of positive, negative, and ambivalent reactions. Positive sentiments often emphasized increased motivation and productivity, while negative responses raised concerns about overreliance and the weakening of foundational skills.

Although many survey respondents reported that GenAI tools had improved their programming abilities, several also expressed concerns about dependency. A few students reported no negative effects, while the most frequently negative effects reported were spending less time thinking through problems, relying too heavily on AI, finding it harder to code from scratch, and copying AI-generated code without fully understanding it.

Among the expert perspectives, one stated that GenAI is not creative, as it generates outputs based on existing statistical patterns rather than producing novel responses derived from intentional reasoning or genuine understanding. Another expert emphasized its practical value in automating routine tasks, allowing developers to focus on complex and creative problem-solving. A third highlighted its educational potential, stressing that GenAI can support learning when used deliberately and tied to specific learning objectives.

**RQ3: How is generative AI reshaping the skill set required for future developers?**

The study highlights that GenAI is contributing to a shift in the skill set expected of future developers. A recurring theme in the YouTube comment sentiment analysis is the phrase "coding is dead," reflecting ongoing uncertainty and discussion about the future role of traditional programming skills. One expert partially supports this view, noting that while many can now generate code using AI tools, not everyone can design robust software. He argues that what distinguishes a developer is the ability to operate at a higher level of abstraction and to design complete systems.

This view is echoed by commenters who emphasize a shift from memorizing syntax toward developing higher-order competencies such as abstraction, system-thinking, communication, and domain knowledge. Another expert reinforces this shift, arguing that future developers must be strong problem-solvers. He highlights skills like algorithmic thinking, contextual awareness, and adaptability, noting that the most critical ability is understanding problems, asking the right questions, and designing effective solutions.

### 5.2 Methodological Limitations and Future Work

The mixed-methods approach used in this thesis captured both broad and detailed perspectives on the topic. However, there are aspects of the methodology that, if further developed, could provide more valuable data and strengthen the study's overall contribution.

The analysis of YouTube comments enabled access to a broad sample of public discourse. Future research could further expand this scope by including comments from multiple videos with varied formats and framings, which may introduce additional perspectives. Incorporating material from other sources such as Reddit, LinkedIn, or relevant online forums could support comparative analysis and help clarify how perceptions vary across contexts. In addition to analyzing existing content, direct participation in online discussions or public debates could allow researchers to pose targeted questions and explore specific viewpoints more interactively.

The survey gave valuable insight into how third-year computer science students at NTNU perceive and engage with GenAI in their learning processes. However, given more time and resources, it would be valuable to widen the sample to include students from additional institutions and countries. This could enable comparisons and reveal differences in how GenAI is perceived and used across educational settings. It would also be interesting to further examine relationships between answers, such as between AI use and engagement to contribute to a more detailed understanding of how students interact with these technologies.

The unstructured interviews allowed participants to reflect freely on their experiences, which suited the exploratory aim of the study and surfaced perspectives that might not have emerged through predefined questions. To build on these findings, future research could incorporate semi-structured or structured interviews to enable more direct comparisons across participants.

The interviews provided valuable insight by capturing open-ended reflections from educators with different experiences of GenAI in teaching. The unstructured format aligned well with the study's exploratory purpose and enabled perspectives to emerge that might not have surfaced through predefined questions. However, with more time and resources, it would have been valuable to expand the interview sample and refine the approach to support deeper comparisons. Incorporating semi-structured or structured interviews could facilitate more consistent responses across participants and improve comparability. Reaching thematic saturation would also help account for variation in teaching contexts, which in this study limited the ability to compare strategies directly. Including additional perspectives such as a teaching assistant who has supported peers both before and after the introduction of GenAI could further enrich the understanding of how educational practices are adapting.

Differences in teaching context among the interviewed educators illustrate the value of a broader sample. Expert 3 taught small, discussion-oriented classes of around 50 students, while Experts 1 and 2 managed large, lecture-based cohorts exceeding 600. These structural contrasts shaped how they experienced student engagement and which strategies were practical to implement. Expanding the sample in future work could offer a more nuanced understanding of how such contextual factors influence the use of GenAI in teaching.

---

## 6. Conclusion

GenAI is influencing many areas of society and it is a global phenomenon. Jobs are disappearing, stock markets are reacting and the technology is changing entire industries. This study has focused on how GenAI is influencing programming education, a small part of the larger picture. Throughout the project, it has become clear that all participants view this as a relevant and pressing issue. No one suggested that GenAI is something that can be ignored.

We are already observing signs of change across several areas. Based on the data we have collected, it is evident that GenAI is affecting how students learn, engage, and think about programming. Among students, GenAI tools are already well integrated into everyday academic work. Educators have varying experiences and perspectives, which is understandable given the complexity and novelty of the topic. Some have already begun adjusting their teaching practices, while others are still exploring the most appropriate ways to respond.

Rather than aiming to draw broad conclusions, this study has examined a specific set of sources to better understand how students, educators, and public discourse are responding to these changes. The observations show a shared understanding across all data sources that GenAI matters. At the same time, there is a diverse range of views on how it should be used and which skills should be emphasized moving forward.

This study has provided insight into how GenAI is influencing programming education in higher education. The findings suggest that this field is in the middle of a transitional phase. Our observations show that students are already familiar with GenAI tools and understand both their potential and their limitations. Educators are also aware of these developments and are beginning to reflect on how such tools might be incorporated into their teaching practices. The observations made throughout this study show that integrating GenAI into lectures and classroom activities can be beneficial, if done thoughtfully and in alignment with clear learning objectives.

### 6.1 Ethical and Sustainability Implications

The use of GenAI in programming education brings up both ethical and sustainability considerations. One ethical concern is the lack of transparency in how GenAI systems work and how their outputs are generated. Users often do not fully understand how the models arrive at their answers, and there is limited control over the accuracy or appropriateness of the outputs. This makes it difficult to evaluate the quality of what is being produced, which can be a problem in an educational context where reliable learning is important.

From a sustainability perspective, GenAI requires a significant amount of computing power. Running large language models consumes energy and water, especially in data centers where cooling is necessary. Some reports estimate that generating a single prompt can use several liters of water, depending on the model and infrastructure (Zewe, 2025). This raises questions about the environmental impact of using GenAI widely in education.

These issues also relate to Sustainable Development Goal 4 (Quality Education), which emphasizes the need for inclusive and high-quality education (Nations, 2024). As programming education evolves with new technologies, academic institutions have a responsibility to ensure that students still learn core competencies and skills that are relevant in society.

### Closing Statement

Thank you for reading our bachelor thesis.

16th May 2025, Trondheim
Julia Vik Remøy & Andrea Amundsen

---

## Bibliography (selected)

Abrahamsson, P., Anttila, T., Hakala, J., Ketola, J., Knappe, A., Lahtinen, D., Liukko, V., Poranen, T., Ritala, T.-M., & Setälä, M. (2024). Chatgpt as a fullstack web developer — early results. XP 2022/2023 Workshops, 201-209.

Balahur, A., et al. (2013). Detecting implicit expressions of sentiment in text: A comparative study. Decision Support Systems, 53(4), 661-671.

Bhimate, H., Nehare, J., Yenchalwar, L., Bhatnagar, Y., & Roy, D. (2024). Unveiling insights: Advanced techniques for youtube comment analysis. International Journal of Engineering Research & Technology, 13(10).

Bommasani, R., Hudson, J. C., et al. (2021). On the opportunities and risks of foundation models. arXiv preprint arXiv:2108.07258.

Bouman, E. (2022). Youtube comment downloader.

Clear, T., Cajander, Å., Clear, A., McDermott, R., Daniels, M., Divitini, M., et al. (2024). AI integration in the IT professional workplace: A scoping review and interview study with implications for education and professional competencies. ITiCSE-WGR 2024, 1-34.

Fiannaca, A. J., Kulkarni, C., Cai, C., & Terry, M. (2023). Programming without a programming language: Challenges and opportunities for designing developer tools for prompt programming. Extended Abstracts of the 2023 CHI Conference on Human Factors in Computing Systems, 1-7.

Fridman, L., & Altman, S. (2024). Lex Fridman Podcast #395: Sam Altman — OpenAI CEO on GPT-4, ChatGPT, and the future of AI.

Groothuijsen, C., Smits, I., Stegeman, I., & van Hattum, P. (2024). Programming in the age of ChatGPT: An exploratory study. Computers & Education: Artificial Intelligence, 5, 100164.

Haindl, M., & Weinberger, A. (2024). Students' experiences of using ChatGPT in an undergraduate programming course. Education and Information Technologies.

Hartley, K., Hayak, M., & Ko, U. H. (2024). Artificial intelligence supporting independent student learning: An evaluative case study of ChatGPT and learning to code. Education Sciences, 14(2), 120.

Hutto, C., & Gilbert, E. (2014). VADER: A parsimonious rule-based model for sentiment analysis of social media text. Proceedings of the International AAAI Conference on Web and Social Media, 8(1), 216-225.

Jing, Y., Wang, H., Chen, X., & Wang, C. (2024). What factors will affect the effectiveness of using ChatGPT to solve programming problems? A quasi-experimental study. Humanities and Social Sciences Communications, 11(1).

Komp-Leukkunen, K., et al. (2024). ChatGPT as a tool for programming education: A literature review and future directions. Education and Information Technologies.

Kothari, C. R. (2004). Research methodology: Methods and techniques (2nd). New Age International.

Kuhn, T. S. (1962). The structure of scientific revolutions. The University of Chicago Press.

Kuramitsu, K., Obara, M., Sato, M., & Akinobu, Y. (2024). Training AI model that suggests Python code from student requests in natural language. Journal of Information Processing, 32, 69-76.

Liu, Y., & Wang, H. (2024, August). Who on earth is using generative AI? World Bank.

Llerena-Izquierdo, J., Gómez, E., et al. (2024). Innovations in introductory programming education: The role of AI with Google Colab and Gemini. Education Sciences, 14(4), 284.

Loria, S. (2018). TextBlob: Simplified text processing.

Miikkulainen, R. (2024). Generative AI: An AI paradigm shift in the making? AI Magazine, 45, 165-167.

Nations, U. (2024). Goal 4: Ensure inclusive and equitable quality education and promote lifelong learning opportunities for all.

Oates, B. J. (2006). Researching information systems and computing. Sage Publications.

OpenAI. (2023a). Best practices for prompt engineering with the OpenAI API.

OpenAI. (2023b). GPT-4 technical report. arXiv:2303.08774.

Phung, T., Pădurean, V.-A., Cambronero, J., Gulwani, S., Kohn, T., Majumdar, R., Singla, A., & Soares, G. (2023). Generative AI for programming education: Benchmarking ChatGPT, GPT-4, and human tutors. arXiv:2306.17156.

Rosenthal, S., Farra, N., & Nakov, P. (2017). SemEval-2017 task 4: Sentiment analysis in Twitter. SemEval, 502-518.

Stolpe, K., & Hallström, J. (2024). Artificial intelligence literacy for technology education. Computers and Education Open, 6, 100159.

Summit, W. G. (2024). Keynote speech by Jensen Huang, CEO of NVIDIA, at the World Government Summit 2024.

Town, N. (2020). Multilingual BERT for sentiment analysis.

Turobov, A., Coyle, D., & Harding, V. (2024). Using ChatGPT for thematic analysis. arXiv:2405.08828.

Wu, J., Liu, W., Zhang, W., Yu, X., & Wu, Z. (2025). Integrating peer assessment cycle into ChatGPT for programming education. Education and Information Technologies.

Yilmaz, R., & Karaoglan Yilmaz, F. G. (2023). The effect of using ChatGPT on students' computational thinking skills and programming self-efficacy. Education and Information Technologies.

Zewe, A. (2025). Explained: Generative AI's environmental impact. MIT News.

---

## Appendix A: Additional Material

The full appendix contains a Jupyter Notebook screenshot documenting the sentiment analysis pipeline (data loading, filtering, application of VADER/TextBlob/BERT, manual classification) and a Google Drive link to the complete YouTube comment datasets and analysis outputs (full and filtered datasets, sentiment scores from all three models, manual sentiment labels, ChatGPT thematic outputs).

The notebook code is omitted from this reference file because it is not stylistically relevant. Only the structural fact that the appendix exists and what it contains is preserved here.
