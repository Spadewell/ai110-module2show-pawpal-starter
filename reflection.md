# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

"""
We need to create classes for the following;

- A `class` for creating a pet profile and adding pet details such as pet owner, pet age, breed, sex, dietary restrictions, allergies, etc.
- A `class` that lets owners create and manage pet tasks such as scheduling walks, meals, medications, vet appointments, grooming, etc. Upon tasks creation, it's assumed that this class also makes it so that the user has the option of storing it as a preference for each of their pet(s) respectively, if more than 1.
- A `class` that suggests daily plans or task schedules for the owner's pet(s), according to both the preferences stored in place for each pet, and any given constraints(these could be the priority of each task, or the time available for each task, according to the availability of the owner), and also including a brief description as to why the suggested plan is a good one. The user still has full control over these task suggestions as they're able to edit them according to their own schedule for the day.

"""

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
