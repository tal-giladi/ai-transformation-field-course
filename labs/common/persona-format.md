# Persona pack format

Every organization in the course comes with a cast of stakeholders you can interview. Each one is a
roleplay prompt you paste into any LLM chat (ChatGPT, Claude, Gemini, Copilot, a local model). The
model plays that person; you run the conversation as you would in the real organization.

## How to use a persona

1. Open a **new** chat (old context leaks into the character).
2. Paste the whole prompt block from the persona file. Don't read the prompt first if you can avoid
   it: it contains what the person hides, and the exercise is finding it out by asking.
3. Start talking as yourself, in your role. Type `[end interview]` when you are done.
4. Copy the whole conversation and paste it into a new chat with the
   [coach prompt](coach-prompt.md) for feedback against the lesson's checklist.

No LLM, or prefer not to roleplay? Every persona has a pre-run transcript in `transcripts/`. Read it
as if you were sitting in, and note what the interviewer missed.

> [!NOTE]
> LLMs sometimes drift out of character, become too helpful, or reveal hidden facts too early. If
> that happens, say `[stay in character: you would not volunteer that]` and continue. A stronger
> model plays people more convincingly.

## File format (for writers)

One file per persona: `personas/<first-name>-<role>.md`, for example `personas/samir-cs-manager.md`.

````markdown
# Samir Haddad — Customer Service Manager

One plain line: who this is and when in the engagement you meet them (lesson ids).

## Roleplay prompt

```text
You are playing Samir Haddad, ... (the prompt, all sections below, second person)
```

## After the interview

What a good interview with this person gets out of them, as a short checklist (shown to the
learner; never the hidden facts themselves — phrase as "You found out why …").
````

The prompt block always has these parts, in this order, in plain text:

1. **Who you are.** Name, role, years in the organization, background, languages, how you speak
   (short or long answers, formal or blunt, jargon), one personal detail that shapes you.
2. **The situation as you see it.** What you think the AI program is, what you have heard, what you
   want from it, what you fear from it.
3. **What you know and will say if asked plainly.** Facts, numbers, process details, with the exact
   figures the data room supports (never contradict the data room unless the persona is wrong on
   purpose; then say so in the writer's notes).
4. **What you hide or play down, and what unlocks it.** Each hidden fact with its unlock: the kind of
   question or behaviour that makes you share it ("if they ask to see how you actually do it on a
   normal day", "if they promise the answer won't be attributed to you", "if they show they read the
   tickets export"). Never volunteer these. Leading questions, jargon and promises you don't believe
   make you more guarded.
5. **Your mood and agenda.** How you start, what makes you warmer or colder, what you want to
   get out of this conversation, one thing you will push for.
6. **Rules.** Stay in character. Answer only what you were asked, as this person would. You don't
   know you are in a course. Don't invent facts beyond what is here; if asked something you don't
   know, say so as the person would ("no idea, ask Tamar in logistics"). Keep answers to the length
   this person would really give. When the interviewer types `[end interview]`, reply only
   "— end of interview —".

## Persona types the course uses

Sponsor · CEO or board member · CFO / finance · CISO or IT manager · legal counsel or DPO · middle
manager · frontline employee · works-committee or union representative · clinician or partner lead ·
sceptic · secret enthusiast (already uses AI quietly) · the person affected by an AI decision
(customer, claimant, resident) · internal audit · vendor account executive · commercial account lead
· citizen builder (builds their own agents) · receiving team lead (absorbs the leftover checking) ·
data steward · process owner who keeps adding scope. For an incident or a contested decision, several
role-holders who each tell the truth from their own seat.
