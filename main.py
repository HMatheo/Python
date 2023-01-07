import openai
import subprocess
import time

openai.api_key = "ta clé api"

model_engine = "text-davinci-003"

def ask_openai(question):
    prompt = f"{question}"

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

while True:

    question = input("Vous: ")
    if question == "exit":
        break

    while True:
        try:
            answer = ask_openai(question)
            break
        except openai.error.ServiceUnavailableError:
            print("Le serveur OpenAI est surchargé ou pas encore prêt. Attente de 5 minutes avant de réessayer...")
            time.sleep(300)
            print("Erreur levée")
        except openai.error.RateLimitError:
            print("Limite de requêtes dépassée. Attente de 5 minutes avant de réessayer...")
            time.sleep(300)
            print("Erreur de limite de requête levée")

    answer = ask_openai(question)
    print("Assistant: ", answer)

    # Enregistrement de la réponse dans un fichier
    if "script" in question.lower() or "programme" in question.lower():
        # Si la question commence par "script" ou "code", vérifier le langage de programmation
        if "python" in question.lower():
            extension = "py"
            with open("/home/matheo/Pro/Py/script.py", "a") as f:
                f.write(answer.strip())
        elif "javascript" in question.lower():
            extension = "js"
            with open("/home/matheo/Pro/JS/script.js", "a") as f:
                f.write(answer.strip())
        elif "html" in question.lower():
            extension = "html"
            with open("/home/matheo/Pro/HTML/index.html", "a") as f:
                f.write(answer.strip())
        elif "css" in question.lower():
            extension = "css"
            with open("/home/matheo/Pro/C/style.css", "a") as f:
                f.write(answer.strip())
        elif "java" in question.lower():
            extension = "java"
        elif "c++" in question.lower():
            extension = "cpp"
            with open("~/home/matheo/Pro/CPP/main.cpp", "a") as f:
                f.write(answer.strip())
        elif "c#" in question.lower():
            extension = "cs"
        elif "php" in question.lower():
            extension = "php"
        elif "sql" in question.lower():
            extension = "sql"
        elif "bash" in question.lower():
            extension = "sh"
        elif "ruby" in question.lower():
            extension = "rb"
        elif "go" in question.lower():
            extension = "go"
        elif "c" in question.lower():
            extension = "c"
            with open("/home/matheo/Pro/C/main.c", "a") as f:
                f.write(answer.strip())
        else:
            extension = "txt"
        with open(f"script.{extension}", "a") as f:
            f.write(answer)

        # Si c'est un script C, ouvrir le fichier dans CLion
        if extension == "c":
            subprocess.Popen(["clion", "/home/matheo/Pro/C/main.c"])

        # si c'est un script C++, ouvrir le fichier dans CLion
        elif extension == "cpp":
            subprocess.Popen(["clion", "/home/matheo/Pro/CPP/main.cpp"])

        # Si c'est un script Python, ouvrir le fichier dans PyCharm
        elif extension == "py":
            subprocess.Popen(["pycharm", "/home/matheo/Pro/Py/script.py"])

        # Si c'est un script JavaScript, ouvrir le fichier dans WebStorm
        elif extension == "js":
            subprocess.Popen(["webstorm", "/home/matheo/Pro/JS/script.js"])

        # Si c'est un script HTML, ouvrir le fichier dans WebStorm
        elif extension == "html":
            subprocess.Popen(["webstorm", "/home/matheo/Pro/HTML/index.html"])

        # Si c'est un script CSS, ouvrir le fichier dans WebStorm
        elif extension == "css":
            subprocess.Popen(["webstorm", "/home/matheo/Pro/CSS/style.css"])

    else:
        # Sinon, enregistrer la question et la réponse dans un fichier texte
        with open("conversation.txt", "a") as f:
            f.write(f"Vous: {question}\n")
            f.write(f"Assistant: {answer}\n")






