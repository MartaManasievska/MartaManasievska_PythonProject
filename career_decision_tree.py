class DecisionTreeNode:
    def __init__(self, text, moral_effect, performance_effect, left=None, right=None, outcome_text=None):
        self.text = text
        self.moral_effect = moral_effect
        self.performance_effect = performance_effect
        self.left = left
        self.right = right
        self.outcome_text = outcome_text

# Scenarios for the Programmer (Software Engineer)
software_eng_tree = {
    1: [
        DecisionTreeNode(
            "Major Production Outage: Your company’s website goes down unexpectedly, and the entire engineering team is scrambling to fix it. You’re in charge of finding the root cause.",
            0, 0,
            left=DecisionTreeNode(
                "You quickly identify the issue using logs and pinpoint a server configuration error. (Fix the issue efficiently)",
                15, 20,
                outcome_text="Great job! You saved the day and earned some praise from the leadership team."
            ),
            right=DecisionTreeNode(
                "You panic and spend time trying to fix the wrong thing. (Delay in fixing the issue)",
                -15, -25,
                outcome_text="The issue isn’t resolved quickly, causing stress for the team."
            )
        ),
        DecisionTreeNode(
            "Your project manager asks you to implement a last-minute feature just before the project deadline. The feature will require significant changes to the codebase.",
            0, 0,
            left=DecisionTreeNode(
                "You implement it in time without compromising quality.",
                10, 15,
                outcome_text="Perfect! You meet the deadline and impress your team with your ability to deliver under pressure."
            ),
            right=DecisionTreeNode(
                "You cut corners to finish on time, causing bugs and crashes.",
                -10, -20,
                outcome_text="Not good! You'll likely have to work overtime to fix the mess."
            )
        ),
        DecisionTreeNode(
            "Your code review feedback is harsh, and your senior developer points out several areas where you need improvement. You feel your work is being unfairly criticized.",
            0, 0,
            left=DecisionTreeNode(
                "You take the feedback professionally and learn.",
                5, 10,
                outcome_text="Excellent growth mindset! You gain respect from your team and improve your skills."
            ),
            right=DecisionTreeNode(
                "You argue with the reviewer, defending your approach and refusing to make changes.",
                -5, -10,
                outcome_text="This might sour your relationship with the senior developer."
            )
        )
    ],
    2: [
        # Day 2 scenarios for Software Engineer
        DecisionTreeNode(
            "A colleague repeatedly misses deadlines, and it’s affecting the team’s progress. You decide to confront them.",
            0, 0,
            left=DecisionTreeNode(
                "You have a calm, constructive conversation and agree on a solution.",
                10, 5,
                outcome_text="Great job! You saved the project while maintaining a healthy relationship."
            ),
            right=DecisionTreeNode(
                "You get frustrated and yell at them, worsening the situation.",
                -10, -10,
                outcome_text="This could create a toxic environment and damage your relationship."
            )
        ),
        DecisionTreeNode(
            "You’re juggling multiple tasks with competing deadlines. Your manager assigns you a high-priority task, but it conflicts with an urgent bug fix requested by a customer.",
            0, 0,
            left=DecisionTreeNode(
                "You prioritize the customer’s bug fix and resolve it immediately.",
                5, 10,
                outcome_text="You ensure customer satisfaction, but now you’ll need to manage your time carefully."
            ),
            right=DecisionTreeNode(
                "You attempt to work on both tasks simultaneously, but your focus is split.",
                -5, -10,
                outcome_text="The quality of your work suffers, and your manager notices."
            )
        ),
        DecisionTreeNode(
            "You receive vague requirements from the product team and build a feature based on your understanding. After completing it, the product team tells you it’s not what they wanted.",
            0, 0,
            left=DecisionTreeNode(
                "You calmly go back to the drawing board, re-clarify the requirements, and implement the feature.",
                5, 5,
                outcome_text="You handle the situation professionally, although it takes extra time."
            ),
            right=DecisionTreeNode(
                "You push back, insisting that your interpretation was correct.",
                -5, -5,
                outcome_text="This leads to frustration and delays the project further."
            )     
        )
    ],
        3: [
        DecisionTreeNode(
            "External Developer Collaboration: You need to collaborate with an external developer on a feature, but they are unresponsive and the deadline is fast approaching.",
            0, 0,
            left=DecisionTreeNode(
                "You proactively take charge of the situation, finding ways to work around the unresponsive developer and still meet the deadline.",
                10, 15,
                outcome_text="Your resourcefulness impresses the team and ensures project success."
            ),
            right=DecisionTreeNode(
                "You wait for the external developer to respond, delaying the project and missing the deadline.",
                -10, -15,
                outcome_text="This delay frustrates your team and reflects poorly on your time management."
            )
        ),
        DecisionTreeNode(
            "Ethical Dilemma with Code: You discover a piece of code in your project is potentially unethical but removing it would delay the project significantly.",
            0, 0,
            left=DecisionTreeNode(
                "You flag the issue immediately and suggest a solution to remove the unethical code, even if it delays the project.",
                15, 10,
                outcome_text="You uphold ethical standards, earning the respect of your colleagues."
            ),
            right=DecisionTreeNode(
                "You decide to ignore the ethical concern, fearing the project delay.",
                -15, -10,
                outcome_text="This decision might lead to negative consequences for the project."
            )
        ),
        DecisionTreeNode(
            "Burnout from Overwork: You've been working overtime for weeks and have an important presentation coming up, but you feel exhausted.",
            0, 0,
            left=DecisionTreeNode(
                "You talk to your manager about the workload and request support or delegation to recharge.",
                10, 5,
                outcome_text="Smart move! You protect your mental health and still deliver a strong presentation."
            ),
            right=DecisionTreeNode(
                "You push through and do the presentation while mentally and physically exhausted.",
                -10, -5,
                outcome_text="You manage to make it through, but the burnout will catch up with you later."
            )
        )
    ],
        4: [
        DecisionTreeNode(
            "Company Merger: Your company is merging with another, and there's uncertainty about your job security. Your role may be redundant.",
            0, 0,
            left=DecisionTreeNode(
                "You start networking within the new organization, offering your skills and value to leadership.",
                10, 15,
                outcome_text="Smart! You make yourself indispensable and navigate the merger smoothly."
            ),
            right=DecisionTreeNode(
                "You sit back and wait for things to unfold, not taking any proactive steps.",
                -10, -15,
                outcome_text="You risk being overlooked in the new structure, potentially losing your position."
            )
        ),
        DecisionTreeNode(
            "Code Freeze Day: It’s code freeze day, and you’re behind on finishing your feature. The rest of the team has completed their work, and you’re the last one left.",
            0, 0,
            left=DecisionTreeNode(
                "You stay focused, work efficiently, and finish the feature just in time for the code freeze.",
                10, 15,
                outcome_text="You meet the deadline and contribute to the overall success of the release."
            ),
            right=DecisionTreeNode(
                "You rush through the final steps, introducing bugs that cause issues in the final product.",
                -10, -15,
                outcome_text="This could lead to a delayed release and additional work to fix your mistakes."
            )
        ),
        DecisionTreeNode(
            "Hacker Attack: Your company’s internal systems have been compromised by a hacker, and you are on the front lines trying to mitigate the damage.",
            0, 0,
            left=DecisionTreeNode(
                "You quickly work with the security team to identify and fix the vulnerability.",
                15, 20,
                outcome_text="Excellent crisis management! You helped prevent significant damage."
            ),
            right=DecisionTreeNode(
                "You panic, fail to isolate the attack, and it spreads across the system, causing severe disruption.",
                -15, -20,
                outcome_text="This leads to a major incident that requires extensive damage control."
            )
        )
    ],
        5: [
        DecisionTreeNode(
            "Debugging a Critical Bug: You’re working on a major project with a tight deadline, and a critical bug in the system has been reported.",
            0, 0,
            left=DecisionTreeNode(
                "You dive deep into the code, use debugging tools, and solve the bug.",
                10, 15,
                outcome_text="Good job! You fixed the bug and still have time to complete other tasks."
            ),
            right=DecisionTreeNode(
                "You apply a temporary fix and hide the issue from your team.",
                -15, -10,
                outcome_text="Not the best choice. This will likely cause issues later and damage your reputation."
            )
        ),
        DecisionTreeNode(
            "Sudden Leadership Opportunity: Your manager asks you to step into a temporary leadership role to guide the team through a high-stakes project.",
            0, 0,
            left=DecisionTreeNode(
                "You embrace the challenge and provide support and guidance to your teammates.",
                15, 20,
                outcome_text="You shine in the leadership role and gain the trust of both your team and higher-ups."
            ),
            right=DecisionTreeNode(
                "You hesitate and pass the opportunity back to your manager.",
                -10, -10,
                outcome_text="You miss a chance to step up, which might affect how others perceive you."
            )
        ),
        DecisionTreeNode(
            "Invited to a Team-Building Event: Your manager encourages you to attend a team-building event, but it’s optional.",
            0, 0,
            left=DecisionTreeNode(
                "You decide to attend and actively participate.",
                10, 5,
                outcome_text="You bond with your team and make connections across the company."
            ),
            right=DecisionTreeNode(
                "You decide not to attend and use the time to catch up on work.",
                -5, 5,
                outcome_text="You’re productive but miss out on team bonding."
            )
        )
    ]
}


# Day 1 Scenarios for the Lawyer
lawyer_tree = {
    1: [
        # Scenario 1
        DecisionTreeNode(
            "Preparing for a High-Profile Trial: You’ve been assigned to defend a wealthy client accused of insider trading. "
            "The evidence seems stacked against your client, but you believe there are loopholes you can exploit.",
            0, 0,
            left=DecisionTreeNode(
                "You dig deeper into the evidence and uncover a key document that suggests the prosecution's main witness might be lying.",
                10, 15,
                outcome_text="Good decision. You’ve found a potential game-changer that could swing the case in your favor."
            ),
            right=DecisionTreeNode(
                "You focus on preparing your client’s testimony, hoping they can convince the jury of their innocence.",
                -5, -10,
                outcome_text="Hmm... This might be a risky strategy. The case could go south fast."
            )
        ),
        # Scenario 2
        DecisionTreeNode(
            "A Conflict of Interest: You learn your spouse is involved with the opposing party’s company, and they didn’t disclose it to you.",
            0, 0,
            left=DecisionTreeNode(
                "You inform your client and the court of the conflict, stepping aside to maintain integrity.",
                10, 5,
                outcome_text="Good decision. You’ve maintained your professional ethics and protected your reputation."
            ),
            right=DecisionTreeNode(
                "You choose not to disclose the conflict, believing you can handle the case fairly.",
                -10, -15,
                outcome_text="Hmm… If the conflict is discovered later, it could damage your credibility."
            )
        ),
        # Scenario 3
        DecisionTreeNode(
            "After-Work Drinks: A prosecutor friend asks for inside information about someone from your close-knit circle. They say, 'You’d be doing me a huge favor…'",
            0, 0,
            left=DecisionTreeNode(
                "You refuse to give them any information, reminding them of professional boundaries.",
                10, 10,
                outcome_text="Good call. You upheld your ethical responsibilities and kept your professional integrity intact."
            ),
            right=DecisionTreeNode(
                "You reveal a small, seemingly harmless detail to them.",
                -10, -10,
                outcome_text="Risky. Sharing inside information could come back to haunt you."
            )
        )
    ],
    # Day 2 Scenarios for the Lawyer
    2: [
    # Scenario 4: Unforeseen Evidence in a Murder Trial
    DecisionTreeNode(
        "Unforeseen Evidence: A video surfaces showing your client in a different location at the time of the murder, "
        "but it raises more questions about how it came into your hands.",
        0, 0,
        left=DecisionTreeNode(
            "You immediately present the video to the court, exposing a critical flaw in the prosecution's case.",
            15, 20,
            outcome_text="Smart! You’ve caught the prosecution off guard, and your client’s chances just increased dramatically."
        ),
        right=DecisionTreeNode(
            "You keep the video to yourself, worried it could complicate the case further.",
            -10, -15,
            outcome_text="This might backfire. Hiding evidence could jeopardize your reputation."
        )
    ),
    # Scenario 5: Unpopular Client
    DecisionTreeNode(
        "Unpopular Client: A high-profile client accused of misconduct is difficult to work with, frequently making rude comments.",
        0, 0,
        left=DecisionTreeNode(
            "You assert your authority and take control of the case.",
            10, 15,
            outcome_text="You’ve maintained control of the case and your professional reputation."
        ),
        right=DecisionTreeNode(
            "You give in to your client’s demands, letting them dictate the defense.",
            -10, -20,
            outcome_text="The case becomes chaotic, and your reputation takes a hit."
        )
    ),
    # Scenario 6: The Whistleblower
    DecisionTreeNode(
        "The Whistleblower: A colleague confides about a major corporate scandal involving your current client.",
        0, 0,
        left=DecisionTreeNode(
            "You encourage your colleague to go public with the information.",
            10, -5,
            outcome_text="A moral choice. Your client’s case suffers, but your integrity is intact."
        ),
        right=DecisionTreeNode(
            "You advise your colleague to stay quiet and handle it internally.",
            -5, 10,
            outcome_text="You protected your client’s case, but it may create issues later."
        )
    )
],

# Day 3 Scenarios for the Lawyer
    3: [
    # Scenario 7: A Personal Vendetta
        DecisionTreeNode(
            "A Personal Vendetta: A case involves a business tycoon who wronged you years ago. Emotions are high.",
            0, 0,
            left=DecisionTreeNode(
                "You put your emotions aside and fight the case professionally.",
                10, 15,
                outcome_text="You maintain your integrity and ensure a fair trial."
            ),
            right=DecisionTreeNode(
                "You let your vendetta take over, exposing your client’s weaknesses unnecessarily.",
                -10, -20,
                outcome_text="Revenge feels satisfying, but it damages your professional standing."
            )
        ),
        # Scenario 8: Confession During Trial
        DecisionTreeNode(
            "Confession During Trial: Your client admits guilt privately but asks you to continue defending them.",
            0, 0,
            left=DecisionTreeNode(
                "You act in accordance with the law and inform the court.",
                10, -5,
                outcome_text="The ethical choice. You’ve upheld your duties, but the case is lost."
            ),
            right=DecisionTreeNode(
                "You continue defending your client to the best of your ability.",
                -5, 10,
                outcome_text="You argue for acquittal, but the guilt may weigh on you personally."
            )
        ),
        # Scenario 9: Secret Evidence
        DecisionTreeNode(
            "Secret Evidence: You discover a key piece of evidence withheld by the opposing party.",
            0, 0,
            left=DecisionTreeNode(
                "You immediately report the evidence to the court.",
                15, 10,
                outcome_text="You’ve demonstrated integrity, and the evidence tips the case in your favor."
            ),
            right=DecisionTreeNode(
                "You use the evidence as leverage during negotiations.",
                -5, 5,
                outcome_text="This could work, but withholding evidence is risky."
            )
        )
    ],
    4: [
        # Scenario 13: Exposing a Corruption Scandal
        DecisionTreeNode(
            "Exposing a Corruption Scandal: You discover evidence of corruption involving executives at the company you represent.",
            0, 0,
            left=DecisionTreeNode(
                "Expose the corruption, even though it risks ruining your case.",
                15, -10,
                outcome_text="You made the ethical choice, putting justice first at the cost of your case."
            ),
            right=DecisionTreeNode(
                "Bury the evidence to focus on winning the case.",
                -10, 10,
                outcome_text="You protect the case outcome, but your decision may come back to haunt you later."
            )
        ),
        # Scenario 14: A New Law
        DecisionTreeNode(
            "A New Law: A recent law changes the legal landscape and directly affects your client’s case.",
            0, 0,
            left=DecisionTreeNode(
                "Use the new law to your advantage, exploiting its provisions to benefit your client.",
                10, 15,
                outcome_text="Smart move! You’ve skillfully used the new law without crossing any ethical lines."
            ),
            right=DecisionTreeNode(
                "Stick with the old law to avoid appearing opportunistic.",
                -5, 5,
                outcome_text="You avoided risk, but it feels like a missed opportunity."
            )
        ),
        # Scenario 15: The Unexpected Retainer
        DecisionTreeNode(
            "The Unexpected Retainer: A powerful client offers you a substantial retainer to take on a shady business deal.",
            0, 0,
            left=DecisionTreeNode(
                "Turn down the case, recognizing the ethical risks.",
                10, 5,
                outcome_text="You preserved your integrity, avoiding the potential fallout of working with this client."
            ),
            right=DecisionTreeNode(
                "Accept the retainer, promising yourself to stay on the right side of the law.",
                -5, 10,
                outcome_text="You’ve taken the case, but it will be a constant challenge to keep your ethics intact."
            )
        )
    ],
    5: [
        DecisionTreeNode(
        "The Lawyer's Betrayal: After months of defending a client accused of embezzlement, you discover they’ve been lying and are guilty. "
        "They ask you to continue the defense and keep their secrets.",
        0, 0,
        left=DecisionTreeNode(
            "You confront your client about the lies and refuse to continue representing them.",
            15, 10,
            outcome_text="A tough decision, but you’ve chosen integrity over personal gain, and your reputation remains intact."
        ),
        right=DecisionTreeNode(
            "You continue defending them, hoping to secure a favorable outcome despite knowing their guilt.",
            -10, -15,
            outcome_text="This could lead to serious consequences if your role in covering up the truth is revealed."
        )
    ),
    # Scenario 11: Malpractice Lawsuit
        DecisionTreeNode(
            "Malpractice Lawsuit: A former client sues you for malpractice, claiming your representation caused them financial loss.",
            0, 0,
            left=DecisionTreeNode(
                "You gather evidence and build a solid defense, proving your actions were professional and justified.",
                10, 10,
                outcome_text="You’ve made the right move. Your case is strong, and you can prove that you acted in good faith."
            ),
            right=DecisionTreeNode(
                "You settle the case to avoid a public and prolonged trial.",
                5, -5,
                outcome_text="The case ends quietly, but settling may appear as an admission of guilt."
            )
        ),
        # Scenario 12: The Dilemma of a Plea Bargain
        DecisionTreeNode(
            "The Dilemma of a Plea Bargain: Your client faces charges that could result in a life sentence. The prosecution offers a plea deal for a shorter sentence.",
            0, 0,
            left=DecisionTreeNode(
                "You advise your client to accept the plea deal, emphasizing the chance for a lighter sentence.",
                10, 5,
                outcome_text="A pragmatic choice. While not ideal, it avoids the risk of a harsher penalty."
            ),
            right=DecisionTreeNode(
                "You convince your client to reject the plea deal, promising to win at trial.",
                -5, -10,
                outcome_text="A risky bet. If the trial doesn’t go well, your client could face a much harsher sentence."
            )
         )
    ]
}


# Doctor Decision Tree
doctor_tree = {
    1: [
        # Scenario 1: The Misdiagnosis
        DecisionTreeNode(
            "The Misdiagnosis: A patient arrives with flu-like symptoms, but their condition quickly worsens. "
            "You discover they have a life-threatening illness that was missed earlier. How do you proceed?",
            0, 0,
            left=DecisionTreeNode(
                "You immediately inform the patient and their family about the missed diagnosis, apologize for the mistake, and begin urgent treatment.",
                10, -5,
                outcome_text="Honesty is the best policy. You’ve ensured the patient gets the care they need, but this may hurt your reputation."
            ),
            right=DecisionTreeNode(
                "You focus on treating the patient immediately, hoping the issue doesn’t come to light.",
                -5, 10,
                outcome_text="This could lead to a quick resolution, but if the mistake is discovered, you could face a malpractice suit."
            )
        ),
        # Scenario 2: A Terminal Diagnosis
        DecisionTreeNode(
            "A Terminal Diagnosis: A long-term patient’s tests reveal their cancer is now terminal. How do you deliver the news?",
            0, 0,
            left=DecisionTreeNode(
                "You have an open and compassionate conversation, explaining the diagnosis and helping them prepare.",
                15, 5,
                outcome_text="A difficult but compassionate approach. You’ve given the patient dignity and support for their final days."
            ),
            right=DecisionTreeNode(
                "You give a vague answer, avoiding the reality and offering false hope.",
                -10, -10,
                outcome_text="This might buy time, but the patient and their family will feel betrayed when the truth comes out."
            )
        ),
        # Scenario 3: The Overworked Doctor
        DecisionTreeNode(
            "The Overworked Doctor: Your hospital is short-staffed, and fatigue is starting to affect your decision-making. What do you do?",
            0, 0,
            left=DecisionTreeNode(
                "You reach out for help, calling in other specialists to manage the workload.",
                10, 5,
                outcome_text="A smart decision. You’ve kept patient care as your priority, even though it meant asking for support."
            ),
            right=DecisionTreeNode(
                "You decide to power through, even though you feel exhausted.",
                -5, 10,
                outcome_text="Your determination is admirable, but fatigue could lead to mistakes or accidents."
            )
        )
    ],
    2: [
        DecisionTreeNode(
        "Unethical Request: A wealthy patient requests an unnecessary surgery, convinced it will make them look younger. "
        "They offer you a substantial bribe to perform the procedure, despite the significant risks.",
        0, 0,
        left=DecisionTreeNode(
            "You refuse the bribe and explain to the patient why the surgery is unnecessary and risky.",
            10, 5,
            outcome_text="A principled decision. You’ve protected the patient’s well-being and kept your ethical standards intact."
        ),
        right=DecisionTreeNode(
            "You agree to the surgery, knowing it’s unnecessary but believing the patient will pay well.",
            -10, -15,
            outcome_text="This could jeopardize your career and lead to legal action if the surgery goes wrong."
        )
    ),
        # Scenario 5: The Organ Transplant Dilemma
        DecisionTreeNode(
            "The Organ Transplant Dilemma: Two equally deserving patients need an organ transplant, but there’s only one donor. "
            "One patient is young with a bright future, and the other is elderly with only a few years left to live.",
            0, 0,
            left=DecisionTreeNode(
                "Follow hospital protocol and give the organ to the patient most likely to survive long-term.",
                5, 10,
                outcome_text="A logical decision, but it may leave you with moral doubt about the elderly patient."
            ),
            right=DecisionTreeNode(
                "Give the organ to the elderly patient, believing in giving them one last chance.",
                10, -5,
                outcome_text="A compassionate choice, but the younger patient may not have another opportunity."
            )
        ),
        # Scenario 6: Life or Death Decision
        DecisionTreeNode(
            "Life or Death Decision: Two patients need surgery. One has a rare, urgent condition requiring immediate action, "
            "while the other is a well-known public figure with a less urgent but life-threatening injury.",
            0, 0,
            left=DecisionTreeNode(
                "You prioritize the patient with the more urgent condition, despite their anonymity.",
                10, 10,
                outcome_text="A responsible and ethical decision that puts patient care first."
            ),
            right=DecisionTreeNode(
                "You operate on the public figure, knowing it could lead to career opportunities.",
                -5, 15,
                outcome_text="This boosts your reputation, but ethically, you ignored the more urgent case."
            )
        )
    ],
    3: [
        DecisionTreeNode(
        "The Medical Mistake: You discover a significant treatment error made by a colleague that could harm the patient. "
        "You must decide whether to report it.",
        0, 0,
        left=DecisionTreeNode(
            "Inform your colleague immediately, suggesting they correct the mistake and report it to the supervisor.",
            10, 5,
            outcome_text="You’ve protected the patient and strengthened your reputation as a trustworthy colleague."
        ),
        right=DecisionTreeNode(
            "Ignore the mistake, hoping it won’t affect the patient or be noticed.",
            -10, -15,
            outcome_text="A risky choice. If the patient’s condition worsens, the mistake will come back to haunt you."
        )
    ),
        # Scenario 8: The Complicated Diagnosis
        DecisionTreeNode(
            "The Complicated Diagnosis: A patient presents with inconclusive symptoms. Initial tests reveal nothing, but you sense something is wrong.",
            0, 0,
            left=DecisionTreeNode(
                "Take the time to run additional tests to ensure accuracy.",
                10, 5,
                outcome_text="A thorough decision. You’ll likely get the correct diagnosis, though it delays treatment."
            ),
            right=DecisionTreeNode(
                "Make a diagnosis based on your intuition and suggest a treatment plan.",
                -5, 10,
                outcome_text="This could resolve the issue quickly, but if you’re wrong, the patient’s condition could worsen."
            )
        ),
        # Scenario 9: The Secret Relationship
        DecisionTreeNode(
            "The Secret Relationship: You’re treating a patient who turns out to be the spouse of a close colleague. "
            "You discover the patient’s affair is impacting their health. Your colleague has asked you not to mention it.",
            0, 0,
            left=DecisionTreeNode(
                "Respect your colleague’s privacy and focus solely on the patient’s health.",
                5, 5,
                outcome_text="You’ve acted professionally, keeping personal matters separate from your work."
            ),
            right=DecisionTreeNode(
                "Advise the patient to open up to their spouse, hoping it improves their health.",
                10, -5,
                outcome_text="A compassionate choice, but it risks discomfort if your colleague finds out."
            )
        )
    ],
    4: [
    # Day 4 Scenarios for the Doctor
        # Scenario 10: The Disruptive Family
        DecisionTreeNode(
            "The Disruptive Family: You’re treating a critically ill patient, but their family members are arguing about the treatment plan. "
            "You need to make a quick decision under pressure.",
            0, 0,
            left=DecisionTreeNode(
                "You mediate the conversation, explaining the medical options clearly and helping the family reach a joint decision.",
                10, 5,
                outcome_text="You’ve acted with empathy, and your professional guidance helped the family reach a consensus."
            ),
            right=DecisionTreeNode(
                "You make the decision yourself and inform the family afterward.",
                5, 10,
                outcome_text="You made the right medical decision, but it risks alienating the family."
            )
        ),
        # Scenario 11: The Insurance Scandal
        DecisionTreeNode(
            "The Insurance Scandal: A patient needs a life-saving procedure, but the hospital’s insurance company denies coverage.",
            0, 0,
            left=DecisionTreeNode(
                "You fight the insurance company using all legal and ethical resources to get coverage for the patient.",
                15, 5,
                outcome_text="You fought hard for the patient. It’s a long battle, but the right thing to do."
            ),
            right=DecisionTreeNode(
                "You proceed with the treatment anyway, knowing the patient can’t afford it without insurance.",
                10, -10,
                outcome_text="You prioritized the patient, but this could have serious legal consequences."
            )
        ),
        # Scenario 12: The Emergency Room Dilemma
        DecisionTreeNode(
            "The Emergency Room Dilemma: A highly intoxicated patient in critical condition refuses treatment. "
            "Their condition is worsening, and the clock is ticking.",
            0, 0,
            left=DecisionTreeNode(
                "You call for a psychiatric evaluation, hoping intervention will calm the patient down.",
                10, -5,
                outcome_text="You handled the situation carefully, but treatment was delayed."
            ),
            right=DecisionTreeNode(
                "You restrain the patient and begin treatment without their consent.",
                -5, 10,
                outcome_text="You acted in the patient’s best interest, but it may have legal repercussions."
            )
        )
    ],
    5:[
            DecisionTreeNode(
        "Medical Research Controversy: You’re involved in a groundbreaking clinical trial, but some results suggest serious side effects.",
        0, 0,
        left=DecisionTreeNode(
            "You report the inconsistencies immediately, ensuring patient safety comes first.",
            15, 5,
            outcome_text="You acted ethically, but the trial might be halted, disappointing many stakeholders."
        ),
        right=DecisionTreeNode(
            "You suppress the negative results, hoping further testing will resolve the issue.",
            -10, -10,
            outcome_text="A risky choice. If the truth comes out, it could endanger patients and ruin your reputation."
            )
        ),
        # Scenario 14: The Overstepping Specialist
        DecisionTreeNode(
            "The Overstepping Specialist: During a complex operation, a junior surgeon starts questioning your approach and suggests alternatives.",
            0, 0,
            left=DecisionTreeNode(
                "You assert your authority and proceed with the operation as planned.",
                5, 10,
                outcome_text="You’ve taken charge, but this could harm team dynamics."
            ),
            right=DecisionTreeNode(
                "You listen to their suggestions and try their approach.",
                -5, 5,
                outcome_text="You took a risk. If it works, it builds trust; if not, it undermines your judgment."
            )
        ),
        # Scenario 15: The Conflicting Diagnosis
        DecisionTreeNode(
            "The Conflicting Diagnosis: A patient’s symptoms could indicate either a rare disease or a common but serious illness. "
            "Tests are inconclusive, and your decision impacts their treatment.",
            0, 0,
            left=DecisionTreeNode(
                "Treat the more dangerous option, assuming the worst-case scenario.",
                10, -5,
                outcome_text="A safe decision that ensures the patient gets urgent care, though you may be over-treating."
            ),
            right=DecisionTreeNode(
                "Treat for the common illness, but monitor their condition closely.",
                -5, 10,
                outcome_text="A practical choice, but if you’re wrong, it could delay critical treatment."
            )
        )
    ]
}
    


# Youtuber Decision Tree
youtuber_tree = {
    1: [
        # Scenario 1: Sponsorship Offer Gone Wrong
        DecisionTreeNode(
            "Sponsorship Offer Gone Wrong: You receive an offer from a massive corporation to sponsor your channel, "
            "but the brand's reputation has been tarnished by a recent scandal.",
            0, 0,
            left=DecisionTreeNode(
                "You reject the sponsorship, staying true to your values and maintaining the trust of your audience.",
                15, 10,
                outcome_text="Great choice. Your audience respects your decision, and your integrity shines through."
            ),
            right=DecisionTreeNode(
                "You accept the deal, knowing the money will significantly boost your content.",
                -10, 15,
                outcome_text="A risky move. Your bank account grows, but your followers are questioning your ethics."
            )
        ),
        # Scenario 2: A Collaboration You Can't Refuse
        DecisionTreeNode(
            "A Collaboration You Can't Refuse: A bigger YouTuber offers to collaborate, but their content often involves drama and controversy.",
            0, 0,
            left=DecisionTreeNode(
                "You politely decline, staying true to your brand and avoiding the drama.",
                10, 5,
                outcome_text="Smart move. You protect your image and maintain a loyal fanbase."
            ),
            right=DecisionTreeNode(
                "You agree to collaborate, thinking it will help you gain exposure.",
                -5, 10,
                outcome_text="This could grow your audience, but your followers might feel you’re compromising your style."
            )
        ),
        # Scenario 3: The Viral Video Dilemma
        DecisionTreeNode(
            "The Viral Video Dilemma: A video you uploaded has gone viral, but it includes risky or controversial content.",
            0, 0,
            left=DecisionTreeNode(
                "You leave the video up, acknowledging it as part of your creative evolution.",
                -5, 15,
                outcome_text="Your channel grows, but the controversy polarizes your audience."
            ),
            right=DecisionTreeNode(
                "You delete the video to protect your reputation.",
                10, -5,
                outcome_text="You’ve avoided fallout, but some fans accuse you of 'caving' to pressure."
            )
        )
    ],
    2: [
        # Scenario 4: Content Theft
        DecisionTreeNode(
            "Content Theft: Another YouTuber plagiarized your video ideas and editing style, essentially copying your work.",
            0, 0,
            left=DecisionTreeNode(
                "You call them out publicly, sharing your frustration with your audience.",
                5, -5,
                outcome_text="You gain support from your audience, but it could escalate into unnecessary drama."
            ),
            right=DecisionTreeNode(
                "You privately reach out to the YouTuber and ask them to give credit or take the video down.",
                10, 5,
                outcome_text="A diplomatic approach avoids drama and might resolve the issue peacefully."
            )
        ),
        # Scenario 5: The 'Cancel Culture' Threat
        DecisionTreeNode(
            "The 'Cancel Culture' Threat: An old controversial tweet resurfaces, threatening your reputation.",
            0, 0,
            left=DecisionTreeNode(
                "You address it head-on, apologizing and explaining how you've grown since then.",
                15, 5,
                outcome_text="Your audience appreciates your honesty, and you regain trust."
            ),
            right=DecisionTreeNode(
                "You ignore the controversy, hoping it will blow over.",
                -10, -15,
                outcome_text="Silence only fuels the fire, and you may lose sponsorships and followers."
            )
        ),
        # Scenario 6: Going Beyond Your Niche
        DecisionTreeNode(
            "Going Beyond Your Niche: Your audience loves your beauty tutorials, but you’re getting bored and want to start gaming content.",
            0, 0,
            left=DecisionTreeNode(
                "You transition slowly, testing the waters with occasional gaming videos.",
                10, 10,
                outcome_text="A balanced approach. Some fans stick around, and new ones join."
            ),
            right=DecisionTreeNode(
                "You fully commit to gaming content, dropping beauty tutorials altogether.",
                -5, 15,
                outcome_text="A bold move. You may lose loyal fans, but gain a whole new audience."
            )
        )
    ],
        3: [
        # Scenario 7: A Conflict with a Fellow Creator
        DecisionTreeNode(
            "A Conflict with a Fellow Creator: You and another popular YouTuber get into a public argument over differing opinions about a viral trend.",
            0, 0,
            left=DecisionTreeNode(
                "You apologize and try to resolve the disagreement privately, ensuring it doesn’t affect your audience.",
                10, 5,
                outcome_text="You avoid further drama and may even mend your professional relationship, showing maturity."
            ),
            right=DecisionTreeNode(
                "You continue the public spat, making response videos and drawing your audience into the drama.",
                -5, 10,
                outcome_text="This increases views in the short term, but your channel may become synonymous with petty feuds."
            )
        ),
        # Scenario 8: The Ad Revenue Dilemma
        DecisionTreeNode(
            "The Ad Revenue Dilemma: A controversial video on your channel is demonetized by YouTube, leaving you without expected ad revenue.",
            0, 0,
            left=DecisionTreeNode(
                "You pivot to brand deals and merchandise, seeking ways to earn outside of YouTube’s AdSense.",
                10, 10,
                outcome_text="Smart choice. Diversifying your income ensures stability in your career."
            ),
            right=DecisionTreeNode(
                "You upload a similar video, hoping to bypass the system and reclaim your lost revenue.",
                -10, -10,
                outcome_text="You risk harsher penalties or even channel demonetization."
            )
        ),
        # Scenario 9: The Personal Life Leak
        DecisionTreeNode(
            "The Personal Life Leak: A personal aspect of your life is leaked online, and your followers are buzzing with curiosity.",
            0, 0,
            left=DecisionTreeNode(
                "You address it head-on, sharing your side of the story with your followers, ensuring transparency.",
                10, 5,
                outcome_text="Your audience respects your honesty, but invasive questions may persist."
            ),
            right=DecisionTreeNode(
                "You remain silent and continue to focus on your content.",
                5, 0,
                outcome_text="Your audience may respect your privacy, but some fans might feel like you’re hiding something."
            )
        )
    ],
    4: [
        # Scenario 10: The Content Drought
        DecisionTreeNode(
            "The Content Drought: You’re running out of video ideas, and the pressure to upload consistently is weighing on you.",
            0, 0,
            left=DecisionTreeNode(
                "You take a break, letting your creativity recharge before returning with fresh, quality content.",
                10, 5,
                outcome_text="Your audience respects your decision, and your videos are more engaging when you return."
            ),
            right=DecisionTreeNode(
                "You upload filler content just to meet deadlines, sacrificing quality for quantity.",
                -5, 10,
                outcome_text="Short-term gains, but your audience will notice and your channel might suffer."
            )
        ),
        # Scenario 11: An Unexpected Career Opportunity
        DecisionTreeNode(
            "An Unexpected Career Opportunity: A major TV network offers you a show, but it means stepping away from YouTube for a while.",
            0, 0,
            left=DecisionTreeNode(
                "You accept the offer, believing this could expose you to a new audience.",
                -5, 15,
                outcome_text="This elevates your career, but some fans feel abandoned."
            ),
            right=DecisionTreeNode(
                "You reject the offer, staying loyal to YouTube and your current fanbase.",
                10, -5,
                outcome_text="You’ve stayed true to your roots, but passing on the opportunity may limit your growth."
            )
        ),
        # Scenario 12: Negative Comments
        DecisionTreeNode(
            "Negative Comments: A flood of negative comments and hate begins affecting your mental health.",
            0, 0,
            left=DecisionTreeNode(
                "You take a break from social media to regain your peace and perspective.",
                10, -5,
                outcome_text="A good choice for your mental well-being, but you risk losing momentum in the short term."
            ),
            right=DecisionTreeNode(
                "You ignore the comments and focus on creating content that stays true to your vision.",
                5, 5,
                outcome_text="Ignoring the negativity helps, but the trolls may not completely stop."
            )
        )
    ],
        5: [
        # Scenario 13: Ethical Sponsorship
        DecisionTreeNode(
            "Ethical Sponsorship: A sponsor wants you to promote their product, but it’s something you don’t truly believe in or use.",
            0, 0,
            left=DecisionTreeNode(
                "You decline the deal, valuing authenticity and the trust of your audience.",
                15, 10,
                outcome_text="Your integrity shines through, and your audience appreciates your honesty."
            ),
            right=DecisionTreeNode(
                "You accept the sponsorship but make it clear to your audience that you were paid to promote it.",
                5, 5,
                outcome_text="Your honesty maintains trust, but some may still feel like you’re selling out."
            )
        ),
        # Scenario 14: Your First Brand Deal
        DecisionTreeNode(
            "Your First Brand Deal: You land your first big sponsorship, but the brand wants changes that compromise your content style.",
            0, 0,
            left=DecisionTreeNode(
                "You accept the changes, knowing the money and exposure will be beneficial.",
                -5, 15,
                outcome_text="You gain financially, but your content may lose the authenticity your audience loves."
            ),
            right=DecisionTreeNode(
                "You reject the changes and negotiate for a more organic integration.",
                10, 5,
                outcome_text="This shows you value your vision, and the brand respects your boundaries."
            )
        ),
        # Scenario 15: Facing Burnout
        DecisionTreeNode(
            "Facing Burnout: You’ve been uploading daily, but the pressure is starting to take a toll on your health and creativity.",
            0, 0,
            left=DecisionTreeNode(
                "You reduce your upload schedule and prioritize self-care.",
                10, 5,
                outcome_text="This helps you recover, and your audience respects your honesty in taking care of yourself."
            ),
            right=DecisionTreeNode(
                "You push through, ignoring the burnout and continuing to upload at the same pace.",
                -10, -15,
                outcome_text="Your creativity and quality dip, and your mental health starts to suffer."
            )
        )
    ]
}


# Actor Decision Tree
actor_tree = {
    1: [
        # Scenario 1: The Career-Defining Role
        DecisionTreeNode(
            "The Career-Defining Role: You’ve been offered the lead role in a major blockbuster film, but the character is controversial and could spark public backlash.",
            0, 0,
            left=DecisionTreeNode(
                "You accept the role, believing this could be your big break, regardless of the potential controversy.",
                -5, 15,
                outcome_text="Your career could skyrocket, but you may face criticism from certain audiences."
            ),
            right=DecisionTreeNode(
                "You turn down the role, not wanting to risk your reputation or get involved in a divisive character.",
                10, -5,
                outcome_text="You preserve your image, but you might miss out on a huge opportunity."
            )
        ),
        # Scenario 2: Typecasting Dilemma
        DecisionTreeNode(
            "Typecasting Dilemma: You’ve been offered a serious drama role after years of playing similar romantic leads, but you’re worried about alienating your fanbase.",
            0, 0,
            left=DecisionTreeNode(
                "You take the drama role to prove your acting range and grow as an artist.",
                10, 15,
                outcome_text="Bold move. You may earn critical acclaim and attract new audiences."
            ),
            right=DecisionTreeNode(
                "You stick with another romantic comedy to maintain your current popularity.",
                5, -5,
                outcome_text="You’ve played it safe, but you risk being typecast and limiting your growth."
            )
        ),
        # Scenario 3: The Difficult Director
        DecisionTreeNode(
            "The Difficult Director: You’re cast in a film with a renowned but notoriously demanding director.",
            0, 0,
            left=DecisionTreeNode(
                "You embrace the challenge, determined to learn and grow under their leadership.",
                -5, 15,
                outcome_text="You may thrive under pressure and deliver a career-defining performance, but the stress takes its toll."
            ),
            right=DecisionTreeNode(
                "You decline the project to protect your mental and emotional well-being.",
                10, -5,
                outcome_text="You’ve prioritized your peace, but you may be seen as unable to handle tough situations."
            )
        )
    ],    
    2: [
        # Scenario 4: The Rival Actor
        DecisionTreeNode(
            "The Rival Actor: A rival actor is up for the same role you’ve been eyeing for months, and the studio needs to decide quickly.",
            0, 0,
            left=DecisionTreeNode(
                "You focus on your craft, letting your performance speak for itself.",
                10, 10,
                outcome_text="Your talent shines through, and you prove yourself as the right choice for the role."
            ),
            right=DecisionTreeNode(
                "You play mind games and try to undermine your rival’s chances.",
                -10, 5,
                outcome_text="This risky move could backfire and damage your reputation as a professional."
            )
        ),
        # Scenario 5: The Controversial Scene
        DecisionTreeNode(
            "The Controversial Scene: You’re required to perform a controversial scene that may be misunderstood by the public.",
            0, 0,
            left=DecisionTreeNode(
                "You agree to the scene, believing in its artistic integrity and the director’s vision.",
                -5, 15,
                outcome_text="You gain praise for your commitment, but you face intense public scrutiny."
            ),
            right=DecisionTreeNode(
                "You ask to modify the scene, standing your ground on your personal values.",
                10, 0,
                outcome_text="You avoid compromising your values, but it may cause tension with the director."
            )
        ),
        # Scenario 6: Public Scandal
        DecisionTreeNode(
            "Public Scandal: A personal scandal breaks out, and it’s starting to impact your career and public image.",
            0, 0,
            left=DecisionTreeNode(
                "You address the scandal publicly, apologizing and explaining your side of the story.",
                10, -5,
                outcome_text="Your maturity and accountability are praised, but rebuilding trust will take time."
            ),
            right=DecisionTreeNode(
                "You stay silent, hoping the media will move on and the controversy will blow over.",
                -10, 5,
                outcome_text="This approach risks making the situation worse, as silence can be seen as avoidance."
            )
        )
    ],
        3: [
        # Scenario 7: The Award Season Pressure
        DecisionTreeNode(
            "The Award Season Pressure: You’ve been nominated for an Oscar, but the pressure to win is overwhelming and starting to affect your personal life.",
            0, 0,
            left=DecisionTreeNode(
                "You focus on enjoying the experience, knowing that being nominated is a huge achievement.",
                10, 5,
                outcome_text="You enjoy the moment and take the pressure off yourself, leaving a positive impression."
            ),
            right=DecisionTreeNode(
                "You push yourself to win at all costs, ignoring the toll on your mental health.",
                -10, 10,
                outcome_text="The pressure helps you perform, but it drains you emotionally and creatively."
            )
        ),
        # Scenario 8: The Role You Hate
        DecisionTreeNode(
            "The Role You Hate: You’re offered a role in a high-profile movie that doesn’t align with your goals or values, but it pays well.",
            0, 0,
            left=DecisionTreeNode(
                "You take the role for financial stability and exposure, hoping it opens doors for future projects.",
                -5, 15,
                outcome_text="You gain fame and money, but fans who value your artistic integrity may feel disappointed."
            ),
            right=DecisionTreeNode(
                "You turn down the role, trusting that your career will grow without compromising your values.",
                15, -5,
                outcome_text="A bold decision that earns respect but costs you immediate financial and career benefits."
            )
        ),
        # Scenario 9: Fading Popularity
        DecisionTreeNode(
            "Fading Popularity: Your career has slowed, and you’re not landing as many high-profile roles as before.",
            0, 0,
            left=DecisionTreeNode(
                "You take a break to pursue other passions and recharge creatively.",
                10, 0,
                outcome_text="This refreshes your outlook and could lead to a creative comeback, but you risk losing relevance."
            ),
            right=DecisionTreeNode(
                "You take any roles you can get, even if they don’t align with your talents or goals.",
                -5, 10,
                outcome_text="You stay visible, but low-quality projects may hurt your reputation over time."
            )
        )
    ],
    4: [
        # Scenario 10: Toxic Set Environment
        DecisionTreeNode(
            "Toxic Set Environment: You’re working on a high-budget film, but the set environment is toxic, with constant tension and poor communication.",
            0, 0,
            left=DecisionTreeNode(
                "You stick it out, maintaining professionalism to complete the project.",
                -5, 10,
                outcome_text="You push through and get the job done, but the stress affects your well-being."
            ),
            right=DecisionTreeNode(
                "You confront the producer or director, asking for a more collaborative work environment.",
                10, 5,
                outcome_text="You address the issue head-on, potentially improving the set dynamic but risking friction with the team."
            )
        ),
        # Scenario 11: Turning Down a Sequel
        DecisionTreeNode(
            "Turning Down a Sequel: The franchise that made you famous offers a big contract for a sequel, but you feel drained by the role.",
            0, 0,
            left=DecisionTreeNode(
                "You turn down the sequel, seeking new opportunities that align with your creative goals.",
                15, -5,
                outcome_text="You earn respect for sticking to your values, but fans may feel disappointed."
            ),
            right=DecisionTreeNode(
                "You accept the sequel for the financial benefits and exposure.",
                -5, 15,
                outcome_text="You secure financial stability but risk being stuck in a repetitive role."
            )
        ),
        # Scenario 12: Getting Caught in a Scandal
        DecisionTreeNode(
            "Getting Caught in a Scandal: An off-screen incident involving you goes viral, damaging your public image.",
            0, 0,
            left=DecisionTreeNode(
                "You apologize publicly, taking responsibility for your actions.",
                10, -5,
                outcome_text="Your honesty and maturity are appreciated, but rebuilding trust will take time."
            ),
            right=DecisionTreeNode(
                "You deny everything, hoping the media storm blows over.",
                -10, 0,
                outcome_text="Denying the incident worsens the backlash and makes you seem unaccountable."
            )
        )
    ],    5: [
        # Scenario 13: Ageism in Hollywood
        DecisionTreeNode(
            "Ageism in Hollywood: You’re no longer the 'young' leading star, and roles have started to dry up. You’re being offered supporting roles that feel beneath your abilities.",
            0, 0,
            left=DecisionTreeNode(
                "You accept the roles, knowing they keep you in the game and could lead to more prominent opportunities.",
                5, 10,
                outcome_text="You stay relevant, but the roles may not excite you or fully utilize your talents."
            ),
            right=DecisionTreeNode(
                "You take a break from acting to focus on other ventures, like producing or directing.",
                10, 5,
                outcome_text="You risk being forgotten, but you discover new ways to express your creativity."
            ),
            outcome_text="You push for a lead role in a project you’re passionate about, hoping to make a statement."
        ),
        # Scenario 14: The Bad Review
        DecisionTreeNode(
            "The Bad Review: You receive a scathing review for a film you worked hard on, and many fans are starting to agree with the critic.",
            0, 0,
            left=DecisionTreeNode(
                "You stay silent, letting the work speak for itself and focusing on future projects.",
                5, 5,
                outcome_text="You take the mature approach, though some may feel you’re ignoring valid criticism."
            ),
            right=DecisionTreeNode(
                "You respond publicly, defending your performance and the film.",
                -5, 10,
                outcome_text="Your passion shines through, but some may perceive you as defensive."
            ),
            outcome_text="You take the criticism to heart and work harder on improving your craft."
        ),
        # Scenario 15: Choosing Between Projects
        DecisionTreeNode(
            "Choosing Between Projects: You’re offered two major roles: a big-budget blockbuster and an indie film with an artistically challenging script.",
            0, 0,
            left=DecisionTreeNode(
                "You choose the blockbuster for its fame and financial security.",
                -5, 15,
                outcome_text="You secure financial stability and wide exposure, though it may lack creative fulfillment."
            ),
            right=DecisionTreeNode(
                "You choose the indie film, valuing creativity over fame and aiming for critical acclaim.",
                10, 5,
                outcome_text="You take a risk for artistic growth, potentially earning long-term respect and acclaim."
            ),
            outcome_text="You try to negotiate both roles, hoping to rearrange schedules and balance both projects."
        )
    ]
}



# Swimmer Decision Tree
swimmer_tree = {
    1: [
        # Scenario 1: The Big Competition
        DecisionTreeNode(
            "The Big Competition: You’ve trained for years for the upcoming national championship, but the night before the event, you come down with a fever. You’re not sure if you can race at your best.",
            0, 0,
            left=DecisionTreeNode(
                "You push through the fever, hoping adrenaline will get you through the race.",
                -10, 5,
                outcome_text="You barely finish the race, but your performance is far from your best. You regret not prioritizing your health but feel pride in giving it your all."
            ),
            right=DecisionTreeNode(
                "You withdraw from the competition, prioritizing your health.",
                10, -5,
                outcome_text="You feel like you’ve let down your team and fans, but your decision to rest prevents further damage and speeds up your recovery."
            )
        ),
        # Scenario 2: The Sponsorship Offer
        DecisionTreeNode(
            "The Sponsorship Offer: A major sports brand offers you a lucrative deal, but it requires you to leave the smaller sponsor that’s supported you from the beginning.",
            0, 0,
            left=DecisionTreeNode(
                "You sign the deal with the bigger brand, knowing it could elevate your career financially.",
                -5, 15,
                outcome_text="You gain widespread exposure and financial freedom, but you feel guilty about leaving your original sponsor behind."
            ),
            right=DecisionTreeNode(
                "You decline the offer to stay loyal to your current sponsor, despite the financial allure.",
                10, -5,
                outcome_text="Your decision earns you respect within your community, but you struggle to cover training costs and personal expenses."
            )
        ),
        # Scenario 3: The Media Scandal
        DecisionTreeNode(
            "The Media Scandal: A tabloid publishes an article accusing you of using performance-enhancing drugs. The rumor goes viral.",
            0, 0,
            left=DecisionTreeNode(
                "You immediately release a public statement denying the accusations and demand a drug test.",
                5, 10,
                outcome_text="You clear your name, but the media frenzy continues for weeks, and it takes time to regain the trust of your fans and sponsors."
            ),
            right=DecisionTreeNode(
                "You stay silent and hope the rumors die down on their own.",
                -10, -10,
                outcome_text="The controversy grows, and your silence is interpreted as guilt. Your career takes a hit, and you lose sponsorships and public support."
            )
        )
    ],
        2: [
        # Scenario 4: The Injury
        DecisionTreeNode(
            "The Injury: During an intense training session, you injure your shoulder. Surgery could sideline you for months, but it’s the safest choice.",
            0, 0,
            left=DecisionTreeNode(
                "You undergo surgery immediately, knowing it’s the safest long-term choice.",
                10, -5,
                outcome_text="The recovery process is grueling, but you come back stronger and set a personal best after a few months."
            ),
            right=DecisionTreeNode(
                "You try physical therapy, hoping the injury will heal without surgery.",
                -5, -10,
                outcome_text="The injury doesn’t improve, and it affects your performance. You eventually need surgery, costing you valuable time."
            )
        ),
        # Scenario 5: The Team Selection
        DecisionTreeNode(
            "The Team Selection: The national team has one spot left in your event. Your friend, a fellow swimmer, has consistently placed first.",
            0, 0,
            left=DecisionTreeNode(
                "You confront your friend, telling them you’re ready to fight for the spot and give it your all in the trials.",
                5, 10,
                outcome_text="You win the spot but feel conflicted about straining your friendship."
            ),
            right=DecisionTreeNode(
                "You choose to step back and support your friend, sacrificing your chance for the good of the team.",
                10, -5,
                outcome_text="Your selflessness is admired, but you wonder if you missed a once-in-a-lifetime opportunity."
            )
        ),
        # Scenario 6: The Personal Life vs. Career Struggle
        DecisionTreeNode(
            "The Personal Life vs. Career Struggle: Your significant other asks you to move in together, but it means leaving your current training facility.",
            0, 0,
            left=DecisionTreeNode(
                "You prioritize your relationship, moving in together and sacrificing your ideal training environment.",
                5, -10,
                outcome_text="Your relationship strengthens, but your performance begins to slip."
            ),
            right=DecisionTreeNode(
                "You stay at your training facility, prioritizing your career over your relationship.",
                -5, 10,
                outcome_text="Your performance improves, but the emotional strain causes tension in your personal life."
            )
        )
    ],
    3: [
        # Scenario 7: The Coach Controversy
        DecisionTreeNode(
            "The Coach Controversy: Your long-time coach makes a polarizing comment in the media, and the public is demanding you distance yourself from them.",
            0, 0,
            left=DecisionTreeNode(
                "You publicly support your coach, defending their right to express their opinions.",
                -10, 5,
                outcome_text="You face backlash and lose sponsors, but you maintain loyalty and earn respect from those who admire your integrity."
            ),
            right=DecisionTreeNode(
                "You distance yourself from your coach, stating publicly that you disagree with their comments.",
                5, 10,
                outcome_text="You keep your sponsors, but your relationship with your coach is strained."
            )
        ),
        # Scenario 8: The Sponsorship Conflict
        DecisionTreeNode(
            "The Sponsorship Conflict: A tobacco company offers you a lucrative sponsorship, but it contradicts your values as a health advocate.",
            0, 0,
            left=DecisionTreeNode(
                "You reject the offer, staying true to your principles.",
                10, 5,
                outcome_text="You miss the financial opportunity but gain respect from fans who value your integrity."
            ),
            right=DecisionTreeNode(
                "You accept the offer, convincing yourself it’s just business.",
                -10, 10,
                outcome_text="You gain wealth but face backlash as your fans question your authenticity."
            )
        ),
        # Scenario 9: The False Start
        DecisionTreeNode(
            "The False Start: During a major race, you’re disqualified for a false start, even though you’re sure it wasn’t your fault.",
            0, 0,
            left=DecisionTreeNode(
                "You accept the disqualification and focus on the next race.",
                5, 5,
                outcome_text="You recover mentally and perform well in your next competition, but the unfairness lingers."
            ),
            right=DecisionTreeNode(
                "You protest the decision publicly, calling for a review of the rules.",
                -5, 10,
                outcome_text="You become a controversial figure, gaining supporters but alienating others."
            )
        )
    ],
    4: [
        # Scenario 10: The Retiring Decision
        DecisionTreeNode(
            "The Retiring Decision: After years of competition, your body is showing signs of wear. You need to decide whether to retire or keep pushing for one more shot at a gold medal.",
            0, 0,
            left=DecisionTreeNode(
                "You decide to retire, feeling your body can’t take any more punishment.",
                10, -5,
                outcome_text="You leave the sport with your dignity intact, but you wonder if you could have achieved more."
            ),
            right=DecisionTreeNode(
                "You push through the physical pain and train for another year, hoping to achieve your ultimate goal.",
                -10, 10,
                outcome_text="You make it through the season, but your body breaks down further, leaving your final race bittersweet."
            )
        ),
        # Scenario 11: The Rivalry
        DecisionTreeNode(
            "The Rivalry: Your biggest rival challenges you directly in an upcoming high-profile event. The media hype is overwhelming.",
            0, 0,
            left=DecisionTreeNode(
                "You train harder than ever, determined to beat them and silence the critics.",
                10, 15,
                outcome_text="You win in an epic showdown, and the victory becomes a legendary moment in the sport."
            ),
            right=DecisionTreeNode(
                "You focus on improving your own performance, ignoring the rivalry.",
                5, 5,
                outcome_text="You perform well, but your rival edges you out. The media calls it a 'missed opportunity.'"
            )
        ),
        # Scenario 12: The Sponsorship Temptation
        DecisionTreeNode(
            "The Sponsorship Temptation: A sponsorship deal from an underdog brand requires a misleading marketing approach that doesn’t align with your values.",
            0, 0,
            left=DecisionTreeNode(
                "You decline the deal, staying true to your integrity.",
                15, -5,
                outcome_text="You lose the financial opportunity, but your reputation remains intact."
            ),
            right=DecisionTreeNode(
                "You accept the deal, rationalizing that the product is 'mostly' effective.",
                -10, 10,
                outcome_text="The sponsorship boosts your income, but your credibility takes a hit when the product disappoints."
            )
        )
    ],
    5: [
        # Scenario 13: The Fan Backlash
        DecisionTreeNode(
            "The Fan Backlash: Fans accuse you of being too focused on personal branding and not enough on the sport. You must decide how to respond.",
            0, 0,
            left=DecisionTreeNode(
                "You address the backlash, apologizing and refocusing on the sport.",
                10, 5,
                outcome_text="Your fans appreciate your sincerity, but the experience is a reminder of constant scrutiny."
            ),
            right=DecisionTreeNode(
                "You continue to prioritize your brand, believing it’s key to sustaining your career.",
                -10, 10,
                outcome_text="The backlash grows, but your personal brand becomes more profitable."
            )
        ),
        # Scenario 14: The Mental Health Battle
        DecisionTreeNode(
            "The Mental Health Battle: You’ve been struggling with anxiety and intense pressure before major events. You’re unsure whether to speak publicly or keep it private.",
            0, 0,
            left=DecisionTreeNode(
                "You open up about your struggles, seeking help and inspiring others.",
                15, 5,
                outcome_text="Your vulnerability inspires the community, though being an advocate adds new pressure."
            ),
            right=DecisionTreeNode(
                "You keep your struggles to yourself, pushing through in silence.",
                -5, 10,
                outcome_text="You perform well at times, but the mental strain becomes overwhelming."
            )
        ),
        # Scenario 15: The Personal Sacrifice
        DecisionTreeNode(
            "The Personal Sacrifice: To push your career to the next level, you’re asked to relocate far from home, leaving family and friends behind.",
            0, 0,
            left=DecisionTreeNode(
                "You move, embracing the challenges and sacrifices for the sake of your career.",
                -5, 15,
                outcome_text="The transition is tough, but you reach new heights in your career, despite the homesickness."
            ),
            right=DecisionTreeNode(
                "You stay close to home, prioritizing your personal life over your career.",
                10, -5,
                outcome_text="You achieve some success but wonder if you missed a chance to push yourself further."
            )
        )
    ]
}
