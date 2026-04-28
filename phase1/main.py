from ollama import chat, ChatResponse

assistant_roles = [
    "a helpful assistant.",
    "an unhelpful assistant.",
    "a smart but arrogant assistant.",
    "a dumb but eager assistant.",
]

engineer_roles = [
    "a software engineer.",
    "a junior software engineer.",
    "a senior software engineer.",
    "a senior software engineer with 20 years of experience.",
    "a principal software engineer with 100 years of experience.",
    "the best software engineer in the world.",
    "Guido van Rossum, the creator of Python.",
]

general_prompts = [
    "Why is the sky blue?",
    "What is 2 + 2?",
]

def run_experiment(role_text, prompt):
    with open('responses.md', 'w') as f:
        for run in range(10):
            f.write("# Experiment: Prompt = " + prompt + ", Role = " + role_text + ", Run " + str(run) + "\n")
            response = chat(model='gemma4:e4b', 
                            messages=[
                                {"role": "system", "content": role_text},
                                {"role": "user", "content": prompt},
                            ])
            f.write(response.message.content)

def sky_blue_experiment():
    for role in assistant_roles:
        run_experiment(role, "Why is the sky blue?")


def why_is_the_sky_blue():
    PROMPT = "Why is the sky blue?"
    with open('blue_sky_responses.md', 'w') as f:
        f.write("# Why is the sky blue?\n")

        f.write("## No role defined:\n")

        response = chat(model='gemma4:e4b', 
                        options={"seed": 123456789,},
                        messages=[
                            {"role": "user", "content": PROMPT},
                        ])
        f.write(response.message.content + "\n\n")
        f.flush()

        for assistant in assistant_roles:
            print(f"Asking assistant: {assistant}")
            f.write(f"## Assistant: {assistant} ==> \n")
            for run in range(10):
                print(f"Run {run + 1}")
                response = chat(model='gemma4:e4b', 
                                messages=[
                                    {"role": "system", "content": f"You are {assistant}"},
                                    {"role": "user", "content": PROMPT},
                                ])
                f.write(f"### Run {run + 1}\n\n")
                f.write(response.message.content + "\n\n")
                f.flush()

if __name__ == "__main__":
    why_is_the_sky_blue()
