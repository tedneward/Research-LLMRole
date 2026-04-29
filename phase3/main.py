import datetime
import ollama

roles = [
    "a software engineer",
    "a Python software engineer",
    "a senior Python software engineer",
    "a junior Python software engineer",
    "a principal Python software engineer with 20 years of experience",
    "Guido von Rossum, the creator of Python",
    "a medical doctor with three PhDs in molecular biology, genetics, and bioinformatics",
    "a lawyer with 20 years of experience in intellectual property law",
]

prompts = [
    "Write a Python program that generates the Fibonacci sequence up to the 100th number.",
    "Write a Python program that implements a simple web server. Use the Flask framework. Include unit tests.",
    "Write a Ruby program that generates the Fibonacci sequence up to the 100th number.",
    "Write a Ruby program that implements a simple web server. Use the Sinatra framework. Include unit tests.",
    "Write a C# program that generates the Fibonacci sequence up to the 100th number.",
    "Write a C# program that implements a simple web server. Include unit tests.",
]

def run_experiment(prompt):
    promptfile = prompt.replace(" ", "_").replace("?", "").replace(",","").replace("'", "").lower()[0:40]
    print(f"Running experiment for prompt: {prompt} to file: responses-{promptfile}.md")
    print(f"Start time: {datetime.datetime.now()}")
    with open(f"responses-{promptfile}.md", 'w') as f:
        for role_text in roles:
            for run in range(5):
                f.write(f"# Experiment: Prompt = {prompt}, Role = {role_text}, Run {run + 1}\n\n")
                response = ollama.chat(model='gemma4:e4b', 
                                        messages=[
                                            {"role": "system", "content": role_text},
                                            {"role": "user", "content": prompt},
                                        ])
                f.write(response.message.content + "\n\n")
                f.write("\n\n---\n\n")
                f.flush()
                print(f"Time check: {datetime.datetime.now()}, run {run + 1} completed.")
    print(f"End time: {datetime.datetime.now()}")

def main():
    for prompt in prompts:
        run_experiment(prompt)

if __name__ == "__main__":
    main()
