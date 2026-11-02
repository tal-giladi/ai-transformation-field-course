// Scenarios for vendor-rfp. A scenario is pure data; `validateScenario` in model.js checks it.
//
// Fields: label, brief, criteria [{ id, label, help, weight }],
//   vendors [{ id, name, tagline, demo, claims [{ id, text, conditions, holds (yes | partly | no), why }],
//     docs [{ title, says }], demoImpression { criterionId: 1–5 } (what the demo suggests),
//     truth { criterionId: 1–5 } (what the evidence supports), poc { metricId: number | null },
//     pocNote, terms { termId: { reply: accepts | refuses, note } }, price, later }],
//   pocIntro, pocMetrics [{ id, label, unit, better: lower | higher }],
//   terms [{ id, label, mustHave, why }], beforeSigning [{ id, label, right, why }],
//   expert { pick, acceptable?: [vendor ids], why }, notes, lessonPoint.
// The evidence ranking (truth) must put the expert's pick first and the demo ranking must not.
// Never assert a legal requirement or deadline as fact: privacy questions go to the DPO and counsel.

export const DEFAULT_PRESET = 'galil';

const galil = {
  label: 'Galil Health — choosing an ambient AI scribe',
  brief:
    'Galil Health runs 14 community clinics in the north of Israel with about 120 doctors and nurses. Patients speak Hebrew, Arabic ' +
    'and Russian, often with a relative in the room. The ask: “an ambient scribe for every doctor”, a tool that listens to the visit ' +
    'and drafts the clinical note. Four vendors have demoed. You score each on six criteria, ask how their headline numbers were ' +
    'measured, run a proof of concept on Galil’s own synthetic visit recordings, then choose a vendor, the contract terms you will ' +
    'require and what happens before anyone signs. Done means a choice you can defend with evidence, and a contract that protects ' +
    'patients’ data.',
  criteria: [
    { id: 'evidence', label: 'Demo vs evidence', help: 'How much of the case is measured, independently, in settings like Galil’s?', weight: 2 },
    { id: 'safety', label: 'Clinical safety', help: 'Omissions, invented findings, how the clinician reviews, a safety case.', weight: 3 },
    { id: 'privacy', label: 'Privacy and data', help: 'Where audio and notes go, training use, retention, sub-processors.', weight: 3 },
    { id: 'languages', label: 'Hebrew, Arabic, Russian', help: 'Performance on real visits in Galil’s languages.', weight: 2 },
    { id: 'integration', label: 'Integration', help: 'Fit with Galil’s clinic record system (Notara) and the effort to connect.', weight: 1 },
    { id: 'contract', label: 'Contract and exit', help: 'Terms, lock-in, price after year one, the vendor’s staying power.', weight: 2 },
  ],
  vendors: [
    {
      id: 'scribewave', name: 'ScribeWave', tagline: 'Large US vendor, used in hundreds of hospitals.',
      demo: 'A polished live demo: a doctor and an actor playing a patient, in English. The structured note appears seconds after the visit ends, already coded.',
      claims: [
        { id: 'acc', text: '98% transcription accuracy', conditions: '200 scripted English visits, a studio microphone, one person speaking at a time, US accents.', holds: 'no', why: 'Galil’s visits are in three languages, unscripted, with relatives talking over each other and an air conditioner running.' },
        { id: 'time', text: 'Saves doctors 2 hours a day', conditions: 'A survey of 60 early-adopter physicians at two US health systems; self-reported; no comparison group.', holds: 'partly', why: 'Enthusiasts estimating their own time saved. Galil should measure note time before and after.' },
        { id: 'lang', text: 'Supports 30+ languages, including Hebrew', conditions: 'Hebrew is a beta model tested on text read aloud, not on conversations. Arabic is tested on Gulf dialects.', holds: 'no', why: '“Supported” is not “measured on visits like ours”.' },
      ],
      docs: [
        { title: 'Security whitepaper', says: 'Independent security audit report available under NDA.' },
        { title: 'Standard data-processing agreement', says: 'De-identified data may be used to improve the service; opting out needs the enterprise plan. Audio kept 90 days. Hosting in the EU or the US.' },
        { title: 'Customer case study', says: 'A US health system; no numbers on errors.' },
      ],
      demoImpression: { evidence: 4, safety: 4, privacy: 3, languages: 4, integration: 4, contract: 3 },
      truth: { evidence: 2, safety: 3, privacy: 2, languages: 2, integration: 3, contract: 2 },
      poc: { he: 14, ar: 27, ru: 12, omit: 7, invent: 3, edit: 4.5 },
      pocNote: 'Good Russian, usable Hebrew, weak Arabic (Galilee dialects). Seven notes in 100 left out something clinically relevant, mostly medication changes said by a relative.',
      terms: {
        noTraining: { reply: 'accepts', note: 'On the enterprise plan, 18% more.' },
        retention: { reply: 'refuses', note: '90 days of audio is the minimum.' },
        location: { reply: 'refuses', note: 'EU or US only.' },
        subprocessors: { reply: 'accepts', note: 'List published; 30 days’ notice.' },
        exit: { reply: 'accepts', note: 'Export in a standard format.' },
        modelChange: { reply: 'refuses', note: 'Models update continuously.' },
        safety: { reply: 'accepts', note: 'A named clinical safety contact.' },
        audit: { reply: 'accepts', note: 'The audit report, no on-site audit.' },
        priceLock: { reply: 'refuses', note: 'Annual list-price changes.' },
      },
      price: 'About ₪1,150 per clinician a month.',
      later: 'Twelve months later: Hebrew notes are fine, Arabic-speaking doctors stopped using it in month three, the data-location question is still open with the DPO, and the measured saving is about 25 minutes a day, not two hours.',
    },
    {
      id: 'kolrefua', name: 'Kol Refua', tagline: 'Israeli start-up, Hebrew first, 30 people.',
      demo: 'The founder demos in Hebrew with a family doctor from the start-up’s partner clinic. It handles Hebrew medical slang and drug brand names well.',
      claims: [
        { id: 'acc', text: '96% accuracy in Hebrew', conditions: '40 visits in the partner clinic, two doctors, Hebrew only, measured by the start-up itself.', holds: 'partly', why: 'Encouraging for Hebrew, but small, self-measured and not on Arabic or Russian.' },
        { id: 'arabic', text: 'Arabic is coming next quarter', conditions: 'No Arabic model exists yet; the evidence is a roadmap slide.', holds: 'no', why: 'A third of Galil’s visits are in Arabic. A roadmap is not a product.' },
        { id: 'local', text: 'Your data never leaves Israel', conditions: 'The app is hosted in Israel, but the sub-processor annex in its data-processing agreement lists a US speech-recognition service.', holds: 'no', why: 'The audio itself goes to the US. You only find this by reading the annex.' },
      ],
      docs: [
        { title: 'Two-page security summary', says: 'No independent audit yet; one is “planned”.' },
        { title: 'Data-processing agreement', says: 'No training on customer data. Sub-processor annex: Israeli cloud host and a US speech-recognition API.' },
        { title: 'Letter from the partner clinic', says: 'Warm, and written by a clinic that owns shares in the start-up.' },
      ],
      demoImpression: { evidence: 3, safety: 3, privacy: 5, languages: 4, integration: 3, contract: 3 },
      truth: { evidence: 2, safety: 2, privacy: 2, languages: 2, integration: 2, contract: 2 },
      poc: { he: 8, ar: null, ru: 21, omit: 5, invent: 1, edit: 3.5 },
      pocNote: 'The best Hebrew of the four. No Arabic at all; weak Russian. No clinical safety case and no way to flag uncertain passages.',
      terms: {
        noTraining: { reply: 'accepts', note: 'Already in the agreement.' },
        retention: { reply: 'accepts', note: 'Audio deleted after 7 days.' },
        location: { reply: 'refuses', note: 'Not until it replaces the US speech service, “next year”.' },
        subprocessors: { reply: 'accepts', note: 'Will add notice and objection.' },
        exit: { reply: 'accepts', note: 'Export, but no escrow and 18 months of funding left.' },
        modelChange: { reply: 'accepts', note: 'Will notify.' },
        safety: { reply: 'accepts', note: 'Will appoint someone.' },
        audit: { reply: 'refuses', note: 'No certification yet.' },
        priceLock: { reply: 'accepts', note: 'Three years fixed.' },
      },
      price: 'About ₪600 per clinician a month.',
      later: 'Twelve months later: the start-up is bought by a foreign company in month nine and the contract is reassigned; Arabic never shipped, so the Arabic-speaking clinics kept typing their notes.',
    },
    {
      id: 'mednote', name: 'MedNote for Notara', tagline: 'An add-on from the vendor of Galil’s own clinic record system.',
      demo: 'Shown inside Notara itself: the note lands in the right fields with one click. The doctor dictates a summary to the microphone after the patient leaves.',
      claims: [
        { id: 'zero', text: 'Zero integration effort', conditions: 'True for the current Notara version. Two of Galil’s five regions run an older version that needs an upgrade first (about four months).', holds: 'partly', why: 'Best integration of the four, but not zero for Galil.' },
        { id: 'acc', text: '95% accurate', conditions: 'Measured on dictated notes, one clinician speaking to the microphone, not on conversations.', holds: 'no', why: 'An ambient scribe listens to a conversation. Dictation is a different, easier task.' },
        { id: 'free', text: 'Included in your licence for the first year', conditions: 'Year-two pricing is “to be agreed”.', holds: 'partly', why: 'Cheap to start, with no price for year two and no easy way out.' },
      ],
      docs: [
        { title: 'Release notes', says: 'Ambient mode is new in the latest version and labelled “preview”.' },
        { title: 'Existing master agreement with the Notara vendor', says: 'Allows the vendor to use customer data for “product improvement”.' },
      ],
      demoImpression: { evidence: 3, safety: 3, privacy: 4, languages: 3, integration: 5, contract: 4 },
      truth: { evidence: 2, safety: 2, privacy: 3, languages: 1, integration: 5, contract: 2 },
      poc: { he: 19, ar: 31, ru: 26, omit: 11, invent: 2, edit: 6 },
      pocNote: 'In conversation mode, eleven notes in 100 left out something clinically relevant. Doctors spent longer correcting notes than they spend writing them today.',
      terms: {
        noTraining: { reply: 'refuses', note: 'The master agreement’s “product improvement” clause stays.' },
        retention: { reply: 'accepts', note: 'Audio deleted after 30 days.' },
        location: { reply: 'accepts', note: 'Hosted in Israel.' },
        subprocessors: { reply: 'accepts', note: 'Listed.' },
        exit: { reply: 'accepts', note: 'Notes stay in Notara anyway.' },
        modelChange: { reply: 'refuses', note: 'Changes ship with Notara releases.' },
        safety: { reply: 'accepts', note: 'Through the existing support contract.' },
        audit: { reply: 'accepts', note: 'Existing certification.' },
        priceLock: { reply: 'refuses', note: 'Year two to be agreed.' },
      },
      price: 'Free in year one; year two to be agreed.',
      later: 'Twelve months later: smooth where Notara was current, but doctors spent longer fixing conversation notes than writing their own; use fell to a few enthusiasts, and year-two pricing arrived at ₪900 per clinician a month.',
    },
    {
      id: 'rishma', name: 'Rishma Health', tagline: 'European specialist, 200 people, in production in three Israeli clinics.',
      demo: 'A plainer demo: a recorded, consented visit in Arabic and Hebrew. The draft note marks the passages where the model was unsure, and the doctor must confirm each one.',
      claims: [
        { id: 'omit', text: 'Leaves out a clinically relevant fact in 2.1% of notes', conditions: 'Independent evaluation by a university hospital: 1,200 primary-care visits in four languages including Arabic, real rooms, every note reviewed by a clinician.', holds: 'yes', why: 'Independent, measured on conversations, in settings close to Galil’s.' },
        { id: 'hebrew', text: 'Hebrew in production in three Israeli clinics', conditions: 'Three clinics for 14 months; references available. Russian evaluated on 150 visits.', holds: 'yes', why: 'Checkable references in Israel.' },
        { id: 'time', text: 'Saves 40–70 minutes a day', conditions: 'A time-and-motion study inside the same evaluation, with a comparison group.', holds: 'partly', why: 'Better evidence than a survey; Galil should still measure its own.' },
      ],
      docs: [
        { title: 'Clinical safety case and hazard log', says: 'Names the hazards (omission, wrong patient, wrong drug) and the controls for each.' },
        { title: 'Independent evaluation report', says: 'Methods, error types and results per language.' },
        { title: 'Data-processing agreement', says: 'No training without opt-in; audio deleted after 30 days; full sub-processor list with notice and objection.' },
        { title: 'Data location', says: 'EU by default; hosting in Israel available at extra cost.' },
        { title: 'Exit schedule', says: 'Data returned in a standard format and certified deletion; six months’ transition.' },
      ],
      demoImpression: { evidence: 3, safety: 3, privacy: 3, languages: 3, integration: 2, contract: 3 },
      truth: { evidence: 4, safety: 4, privacy: 4, languages: 4, integration: 3, contract: 4 },
      poc: { he: 9, ar: 11, ru: 10, omit: 2, invent: 0.5, edit: 3 },
      pocNote: 'Consistent across all three languages. Two notes in 100 left out something relevant, and most of those were flagged as unsure. Integration with Notara needs a project through Notara’s interface (about three months).',
      terms: {
        noTraining: { reply: 'accepts', note: 'Default.' },
        retention: { reply: 'accepts', note: 'Default 30 days.' },
        location: { reply: 'accepts', note: 'Israel hosting, about 8% more.' },
        subprocessors: { reply: 'accepts', note: 'Default.' },
        exit: { reply: 'accepts', note: 'Default.' },
        modelChange: { reply: 'accepts', note: 'Notice and a re-run on Galil’s test set.' },
        safety: { reply: 'accepts', note: 'Named clinical safety officer.' },
        audit: { reply: 'accepts', note: 'Certification and audit rights.' },
        priceLock: { reply: 'refuses', note: 'Annual indexation.' },
      },
      price: 'About ₪1,300 per clinician a month, plus the integration project.',
      later: 'Twelve months later: rolled out region by region after a six-week clinician pilot; Arabic-speaking clinics adopted fastest; the integration took four months, not three; measured note time fell by about 35 minutes a day.',
    },
  ],
  pocIntro: 'Galil’s data team recorded 90 synthetic visits (actors following real-shaped scripts, 30 per language, with relatives and room noise) and every vendor ran them. A clinician reviewed every note.',
  pocMetrics: [
    { id: 'he', label: 'Hebrew word error rate', unit: '%', better: 'lower' },
    { id: 'ar', label: 'Arabic word error rate', unit: '%', better: 'lower' },
    { id: 'ru', label: 'Russian word error rate', unit: '%', better: 'lower' },
    { id: 'omit', label: 'Clinically relevant facts left out, per 100 notes', unit: '', better: 'lower' },
    { id: 'invent', label: 'Invented findings, per 100 notes', unit: '', better: 'lower' },
    { id: 'edit', label: 'Minutes for the clinician to correct a note', unit: 'min', better: 'lower' },
  ],
  terms: [
    { id: 'noTraining', label: 'No use of our audio, transcripts or notes to train or improve models, de-identified included', mustHave: true, why: 'De-identified health data can often be re-identified, and once it trains a model it cannot be taken back.' },
    { id: 'retention', label: 'Audio deleted within 30 days of the note being signed', mustHave: true, why: 'The audio is the most sensitive copy and nobody needs it once the note is signed.' },
    { id: 'location', label: 'Stored and processed in Israel, or where Galil’s DPO approves in writing', mustHave: true, why: 'Where health data may go is a question for the DPO and counsel; the contract must let them decide.' },
    { id: 'subprocessors', label: 'Full sub-processor list, notice before changes, the right to object', mustHave: true, why: 'Kol Refua’s “never leaves Israel” failed in the sub-processor annex.' },
    { id: 'exit', label: 'Data returned in a standard format, certified deletion, six months’ transition', mustHave: true, why: 'Without an exit, year-two pricing is whatever the vendor says.' },
    { id: 'modelChange', label: 'Notice before model changes and a re-run on Galil’s test set first', mustHave: true, why: 'Your proof of concept is only valid for the model you tested.' },
    { id: 'safety', label: 'A named clinical safety officer and incident reporting to Galil within an agreed time', mustHave: true, why: 'Omissions in clinical notes are patient-safety incidents, not support tickets.' },
    { id: 'audit', label: 'Independent security certification and the right to audit', mustHave: false, why: 'Worth having; the certification usually is enough.' },
    { id: 'priceLock', label: 'Price fixed for three years', mustHave: false, why: 'Nice to have; indexation is normal. A good exit clause protects you more.' },
  ],
  beforeSigning: [
    { id: 'dpo', label: 'Send the data-processing agreement, the data-location answer and the sub-processor list to Galil’s DPO and counsel before signing', right: true, why: 'Health data is especially sensitive under Israeli privacy law, and the Ministry of Health has its own rules for health information. Which rules apply and what they require is the DPO’s and counsel’s call, not the vendor’s or yours.' },
    { id: 'pilot', label: 'A six-week clinician pilot in two clinics (one Arabic-speaking) with a stop rule before any rollout', right: true, why: 'Doctors decide whether the tool survives; the pilot measures note time and errors in the real rooms.' },
    { id: 'consent', label: 'Patient information and consent wording agreed by the medical director and the DPO', right: true, why: 'Patients are being recorded. How they are told and asked is not a vendor default.' },
    { id: 'trustVendor', label: 'Rely on the vendor’s written statement that it complies with Israeli law', right: false, why: 'A vendor’s statement is a claim, not evidence, and it does not move responsibility from Galil.' },
    { id: 'bigBang', label: 'Roll out to all 120 clinicians at once to get the volume discount', right: false, why: 'A discount is not a reason to skip the evidence that clinicians will use it safely.' },
  ],
  expert: {
    pick: 'rishma',
    why: 'Rishma is the only vendor whose headline numbers were measured independently on conversations like Galil’s, its proof of concept held in all three languages, and it accepts every must-have term. It looked weakest in the demo, and it costs the most.',
  },
  notes: [
    'Galil Health, Notara and all four vendors are fictional. 14 clinics, about 120 clinicians and the language mix (roughly a third each) are assumptions for this model.',
    'Proof of concept: 90 synthetic visits (30 per language) recorded by actors from real-shaped scripts, with relatives and room noise. Every number in it is invented for teaching.',
    'Prices are illustrative.',
    'The six criteria and their weights (safety and privacy ×3, evidence, languages and contract ×2, integration ×1) stand for what Galil’s steering group agreed before the demos.',
    'No legal requirement is stated as fact: the model sends privacy and data-location questions to the DPO and counsel.',
  ],
  lessonPoint:
    'Score the evidence, not the demo: ask under what conditions every headline number was measured, test the shortlist on your own data in your own languages, and put the protections in the contract (training use, retention, location, sub-processors, model changes, exit), with the DPO and counsel deciding the privacy questions before anyone signs.',
};

// ---------- generic ----------

const generic = {
  label: 'Generic — choosing a call-summary tool for a contact centre',
  brief:
    'A utility’s 600-seat contact centre takes calls in Hebrew, Arabic and English. It wants a tool that summarises each call into the ' +
    'CRM so agents stop typing wrap-up notes. Three vendors have demoed. Score them, ask how their numbers were measured, run a proof ' +
    'of concept on the centre’s own synthetic calls, then choose a vendor, the contract terms and the steps before signing.',
  criteria: [
    { id: 'evidence', label: 'Demo vs evidence', help: 'Measured, independent, on calls like ours?', weight: 2 },
    { id: 'quality', label: 'Summary quality', help: 'Facts left out or invented; how agents check them.', weight: 3 },
    { id: 'privacy', label: 'Privacy and data', help: 'Recordings, training use, retention, sub-processors.', weight: 3 },
    { id: 'languages', label: 'Hebrew, Arabic, English', help: 'On real calls, not read speech.', weight: 2 },
    { id: 'integration', label: 'CRM integration', help: 'Effort to connect and keep connected.', weight: 1 },
    { id: 'contract', label: 'Contract and exit', help: 'Terms, lock-in, price after year one.', weight: 2 },
  ],
  vendors: [
    {
      id: 'summit', name: 'SummIt', tagline: 'Global platform vendor.',
      demo: 'A slick demo on an English sales call: summary, sentiment and next steps in two seconds.',
      claims: [
        { id: 'acc', text: '97% summary accuracy', conditions: 'English sales calls, scored by the vendor’s own model, not by people.', holds: 'no', why: 'A model grading itself, on a different kind of call.' },
        { id: 'aht', text: 'Cuts handling time by 30%', conditions: 'One customer, measured in the first month, when wrap-up was also redesigned.', holds: 'partly', why: 'Two changes at once; no comparison group.' },
      ],
      docs: [{ title: 'Standard terms', says: 'Call data may be used to improve models; recordings kept 12 months.' }],
      demoImpression: { evidence: 4, quality: 4, privacy: 3, languages: 4, integration: 4, contract: 3 },
      truth: { evidence: 2, quality: 3, privacy: 2, languages: 2, integration: 4, contract: 2 },
      poc: { he: 16, ar: 29, en: 7, omit: 9, invent: 4, edit: 1.6 },
      pocNote: 'Fine in English, weak in Arabic; invents a “next step” in four calls out of 100.',
      terms: {
        noTraining: { reply: 'refuses', note: 'Only on the premium tier, not offered here.' },
        retention: { reply: 'refuses', note: '12 months minimum.' },
        subprocessors: { reply: 'accepts', note: 'Published list.' },
        exit: { reply: 'accepts', note: 'Export.' },
        modelChange: { reply: 'refuses', note: 'Continuous updates.' },
      },
      price: 'About ₪85 per seat a month.',
      later: 'A year later: Arabic-speaking agents went back to typing notes; the DPO is still unhappy about the 12-month retention.',
    },
    {
      id: 'callnote', name: 'CallNote for CRM', tagline: 'An add-on from the CRM vendor.',
      demo: 'Shown inside the CRM: the summary fills the case fields automatically.',
      claims: [
        { id: 'zero', text: 'No integration needed', conditions: 'True on the current CRM version, which the centre already runs.', holds: 'yes', why: 'Real advantage.' },
        { id: 'acc', text: '94% accurate', conditions: 'Measured on chat transcripts, not on calls.', holds: 'no', why: 'Text chat is not speech.' },
      ],
      docs: [{ title: 'CRM master agreement', says: 'Customer data may be used for product improvement.' }],
      demoImpression: { evidence: 3, quality: 3, privacy: 4, languages: 3, integration: 5, contract: 4 },
      truth: { evidence: 2, quality: 2, privacy: 3, languages: 2, integration: 5, contract: 2 },
      poc: { he: 18, ar: 33, en: 9, omit: 12, invent: 2, edit: 2.2 },
      pocNote: 'Twelve summaries in 100 missed the reason for the call.',
      terms: {
        noTraining: { reply: 'refuses', note: 'Master agreement clause stays.' },
        retention: { reply: 'accepts', note: '30 days.' },
        subprocessors: { reply: 'accepts', note: 'Listed.' },
        exit: { reply: 'accepts', note: 'Data stays in the CRM.' },
        modelChange: { reply: 'refuses', note: 'Ships with CRM releases.' },
      },
      price: 'Free for six months, then to be agreed.',
      later: 'A year later: agents correct most summaries; the price after six months doubled the CRM bill.',
    },
    {
      id: 'voxa', name: 'Voxa', tagline: 'Specialist in multilingual call summaries.',
      demo: 'A plain demo on a recorded Arabic billing call; uncertain facts are highlighted for the agent.',
      claims: [
        { id: 'omit', text: 'Misses the call reason in 3% of summaries', conditions: 'Independent evaluation on 2,000 utility and telecom calls in five languages, scored by people.', holds: 'yes', why: 'Independent and on calls like ours.' },
        { id: 'aht', text: 'Saves 40 seconds of wrap-up per call', conditions: 'A controlled trial at two contact centres.', holds: 'partly', why: 'Good design; measure your own.' },
      ],
      docs: [{ title: 'Data-processing agreement', says: 'No training without opt-in; recordings deleted after 30 days; sub-processors listed with notice.' }],
      demoImpression: { evidence: 3, quality: 3, privacy: 3, languages: 3, integration: 2, contract: 3 },
      truth: { evidence: 4, quality: 4, privacy: 4, languages: 4, integration: 3, contract: 4 },
      poc: { he: 9, ar: 12, en: 6, omit: 3, invent: 1, edit: 1.1 },
      pocNote: 'Consistent in all three languages; needs a six-week CRM integration.',
      terms: {
        noTraining: { reply: 'accepts', note: 'Default.' },
        retention: { reply: 'accepts', note: 'Default.' },
        subprocessors: { reply: 'accepts', note: 'Default.' },
        exit: { reply: 'accepts', note: 'Export and deletion.' },
        modelChange: { reply: 'accepts', note: 'Notice and re-test.' },
      },
      price: 'About ₪95 per seat a month plus integration.',
      later: 'A year later: wrap-up time down about 35 seconds a call, measured against a comparison team.',
    },
  ],
  pocIntro: 'The centre recorded 150 synthetic calls (actors, real-shaped scripts, 50 per language) and every vendor summarised them; supervisors scored every summary.',
  pocMetrics: [
    { id: 'he', label: 'Hebrew word error rate', unit: '%', better: 'lower' },
    { id: 'ar', label: 'Arabic word error rate', unit: '%', better: 'lower' },
    { id: 'en', label: 'English word error rate', unit: '%', better: 'lower' },
    { id: 'omit', label: 'Summaries missing the call reason, per 100', unit: '', better: 'lower' },
    { id: 'invent', label: 'Summaries with an invented fact, per 100', unit: '', better: 'lower' },
    { id: 'edit', label: 'Minutes for the agent to fix a summary', unit: 'min', better: 'lower' },
  ],
  terms: [
    { id: 'noTraining', label: 'No use of our calls or summaries to train or improve models', mustHave: true, why: 'Customers’ calls are not the vendor’s training data.' },
    { id: 'retention', label: 'Recordings deleted within 30 days', mustHave: true, why: 'Keep the most sensitive copy for as short a time as possible.' },
    { id: 'subprocessors', label: 'Sub-processor list, notice and the right to object', mustHave: true, why: 'You need to know where the audio goes.' },
    { id: 'exit', label: 'Export and certified deletion at exit', mustHave: true, why: 'Protects you at renewal.' },
    { id: 'modelChange', label: 'Notice before model changes and a re-test first', mustHave: false, why: 'Strongly advisable; less critical than in clinical use.' },
  ],
  beforeSigning: [
    { id: 'dpo', label: 'Send the data terms to the DPO and counsel before signing', right: true, why: 'Privacy questions are theirs to decide.' },
    { id: 'pilot', label: 'A four-week pilot with two teams and a comparison team', right: true, why: 'Measure the saving yourself.' },
    { id: 'trustVendor', label: 'Accept the vendor’s compliance statement', right: false, why: 'A claim, not evidence.' },
  ],
  expert: { pick: 'voxa', why: 'Voxa’s numbers were measured independently on calls like ours, it held in the proof of concept in all three languages, and it accepts every must-have term.' },
  notes: ['Every vendor, number and price in this generic preset is fictional and chosen to make the trade-offs visible.'],
  lessonPoint: galil.lessonPoint,
};

export const PRESETS = { galil, generic };
