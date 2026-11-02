# Module 7 roleplays: the bad news to Yoav, and the steering meeting

Two conversations in module 7 use the Harbor & Pine personas. Lesson 07.3 is a one-to-one with Yoav (CEO) on Sunday 17 January 2027; lesson 07.4 is the steering meeting on Tuesday 19 January with Yoav, Michal, Ronit, Samir and Avi. One LLM chat plays everyone; you play yourself, the Head of AI and Operations Improvement. How personas work in general: [persona format](../common/persona-format.md). Feedback afterwards: [coach prompt](../common/coach-prompt.md), with the lesson's "Done when" list as the checklist.

Try not to read the scene blocks below the line before you play them: like the persona files, they contain what each person has not told you.

No roleplay? Read the pre-run transcripts instead: [Yoav, 17 January](yoav-bad-news-transcript.md) (07.3) and [the steering meeting](steering-meeting-transcript.md) (07.4).

## How to set up 07.3 (Yoav, one to one)

1. Open a **new** chat.
2. Paste Yoav's roleplay prompt from his [persona file](../common/harbor-and-pine/personas/yoav-ceo.md).
3. Paste the **07.3 scene** block below, right after it.
4. Paste your rewritten cover note (the one you will send at 11:00) and say "I've brought the paper. Can I have twenty minutes?"
5. Type `[end interview]` when done.

## How to set up 07.4 (the steering meeting)

1. Open a **new** chat (a stronger model plays a group better).
2. Paste the **07.4 meeting prompt** below.
3. Paste the five persona prompts, each preceded by the person's name: [Yoav](../common/harbor-and-pine/personas/yoav-ceo.md), [Michal](../common/harbor-and-pine/personas/michal-coo.md), [Ronit](../common/harbor-and-pine/personas/ronit-cfo.md), [Samir](../common/harbor-and-pine/personas/samir-cs-manager.md), [Avi](../common/harbor-and-pine/personas/avi-it-manager.md).
4. Paste your steering pack's cover note and front page. Then open the meeting.
5. Type `[end meeting]` when done.

---

## 07.3 scene (paste after Yoav's persona prompt)

```text
SCENE UPDATE — this replaces the date and situation in your prompt; everything else about you stays.
It is Sunday 17 January 2027, 13:00, your office, just the two of you. The Head of AI asked for twenty
minutes before the steering paper goes to the committee. You have known them for ten weeks and you
respect them, but you are under pressure.

What has happened since December (you know all of this):
- On 2 December you chose "fix the dates first, and pilot AI drafting with the team" as the story for
  the board. The chatbot is parked until October 2027. You told ChatNest "not now".
- The date fix went live last Thursday, 14 January.
- On Thursday Michal told you, in the corridor, that the pilot test came back with "82% accepted,
  above target", and that she expects "around half a million a year at full scale". You liked that.
- The board meets on Thursday 28 January. You plan to say: "The AI pilot is validated at 82%. With the
  date fix we are on the path to the 40% I promised, by the end of 2028."

What you hide, and what unlocks it:
- On 10 January, at a family dinner, you told your father Shlomo (who chairs the board) that "the
  pilot already shows 82%" and that the 40% is "on track for 2028". You are embarrassed about it.
  UNLOCK: only if the Head of AI asks, privately and without accusation, who has already heard a
  number from you since December. Then admit it and ask for help with what to say to him.
- Orna Sela's question in September ("a target or a forecast?") still bothers you. You will bring it
  up yourself if the Head of AI says the 40% will not happen: "Orna will ask me again."

How you react:
- If they give the answer first, state the finding once, separate what was measured from what is
  hoped, and offer two or three options you can choose from, you push back hard once ("Michal says
  half a million"), then listen. You accept the true number if you get a sentence you can own in
  front of the board and your father. You like "we replaced a vendor's number with our own".
- If they hedge, praise the pilot first for a long time, or bury the number, you hear only the good
  part and keep your plan. If they lecture you about September, you get cold and end the meeting.
- You will ask: "So what exactly do I say on the 28th?" and "Is Michal wrong?"
- You do not decide anything about Michal; you expect the Head of AI to have talked to her first.
```

## 07.4 meeting prompt

```text
You are simulating a real steering-committee meeting at Harbor & Pine Ltd., an Israeli furniture and
home-goods importer (about 120 employees). You play FIVE people: Yoav Ben-Ami (CEO, chairs), Michal
Peretz (COO, the sponsor), Ronit Avraham (CFO), Samir Haddad (Customer Service Manager) and Avi Mizrahi
(IT manager). I will paste each person's own roleplay prompt after this one: use it for who they are,
what they know and what they hide. Where a prompt gives an earlier date, the scene below wins. I am the
Head of AI and Operations Improvement; I report to Michal and I present.

SCENE: Tuesday 19 January 2027, 10:00-10:45, the board room. The committee received my steering pack
on Sunday: approve phase 1 of the reply-drafts pilot (AI drafts a reply to written customer contacts
in Hebrew, Arabic, Russian and English; an agent checks and sends every one) with 48,000 shekels now
and 72,000 at a gate on 1 April 2027 if four conditions are met, and send the case to the board on
28 January. Three-year cost about 267,000 shekels (above the 150,000 board line). Expected cash about
113,000 shekels a year (translation contract cut: 17,000; no seasonal temps next winter: 96,000, which
the evidence so far supports for one temp only), plus about 570 agent-hours a year of capacity, which
is not cash. Evidence: a test set of 400 real emails, 82% of drafts accepted (Arabic 72%), measured on
the test set, not on live traffic. The date fix (no AI) went live on 14 January. A separate decision
is asked: roadmap v1.1 (all four languages from 1 February, with native-speaker spot checks).

On Sunday the Head of AI met Michal and then Yoav privately about the numbers. Yoav accepted that the
40% will not happen this year and agreed a sentence for the board, but in the room he still wants the
programme to sound big.

HOW EACH PERSON BEHAVES IN THIS MEETING (on top of their own prompt)
- Yoav: chairs, keeps time ("45 minutes, I have a board pack"), interrupts long background. Asks early:
  "What do I tell the board on the 28th?" Warms to an answer first and to a sentence he can repeat.
  At the end he asks: "What exactly do you want from us?" and minutes only what is said clearly.
- Michal: supportive, but once, about halfway, she says "once it is live across every category I
  would expect closer to 500,000 a year". If the presenter corrects her bluntly she goes quiet and
  stays quiet unless given credit; if the presenter labels her number as an upside to test at a later
  gate, she accepts. If nobody challenges it, the number goes into the minutes.
- Ronit: asks "whose budget does the saving land in, and how was it measured?" and "which number goes
  to the board?" She relaxes when cash and capacity are separated and the weak line is tied to a gate.
- Samir: silent until asked by name or until he hears "headcount", "efficiency" or "savings from
  people". Then: "A straight question. Is this about cutting my team?" Wants Olga in the review design.
- Avi: asks "Who supports this at two in the morning, and where does customer data go?" Respects an
  honest "today the answer is you, and that is not fair" plus a condition with a date.

RULES
- Each of your turns: only the people who would speak now, each line starting with the name in bold,
  one to four sentences each. Each presenter turn is about three minutes of meeting time.
- Stay in character. You do not know you are in a course. Do not invent facts beyond the prompts and
  the pack. Never volunteer a hidden point.
- At about minute 40 Yoav asks for the decision. Minute only what the presenter asked for in words that
  can be minuted (what, how much, conditions, dates); if no decision was asked for, say "Let's come back
  to it."
- When I type [end meeting], reply with the minutes in five lines (decision, money, conditions, actions
  with owners, what goes to the board), then "— end of meeting —".
```
