import openai

# OpenAI API key
# get your own: https://platform.openai.com/api-keys
openai.api_key = "YOUR_OWN_API_KEY_HERE"

# generating text summary
# length: short or detailed
# language: user can choose
def summarize_text(text, language="English", length="short"):
    try:

        # prompt for an AI model
        prompt = f"Summarize this text in {length} format in {language}:\n{text}"

        # response by an AI model
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes texts."},
                {"role": "user", "content": prompt}
            ], 
            temperature=0.5
        )

        # summary from the response
        summary = response['choices'][0]['message']['content']
        return summary
    except Exception as e:
        return f"Error: {str(e)}"


# reads text from .txt file
def read_text_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"Error: {str(e)}"

# saves summary to .txt file
def save_summary_to_file(summary, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(summary)
        print(f"Summary saved to the file: {file_path}")
    except Exception as e:
        return f"Error: {str(e)}"


# function which runs the program
def main():
    print("---Text Summarizer---")
    print("Choose the option:")
    print("1. Enter the code manually")
    print("2. Read text from the .txt file")
    print("3. Exit")

    while True:
        option = input("\nYour choice (1/2/3): ")

        # write the text manually
        if option == "1":
            user_text = input("\nEnter the text to summarize: ")

            # Language option
            language = input("\nChoose the language of the summary (English/Polish: ")
            if language not in ["English", "Polish"]:
                language = "English"  # default language

            # Length option
            length = input("\nChoose the length of summary (short/detailed): ").lower()
            if length not in ["short", "detailed"]:
                length = "short"  # default length

            # Summary generating
            summary = summarize_text(user_text, language, length)
            print("\nSummary:")
            print(summary)

            # File save option
            save_option = input("\nShould summary be saved to the file? (yes/no): ").lower()
            if save_option == "yes":
                file_path = input("Enter the file name (ex. summary.txt): ")
                save_summary_to_file(summary, file_path)

        # Read from the .txt file
        elif option == "2":
            file_path = input("\nEnter the file path .txt: ")
            user_text = read_text_from_file(file_path)

            if "Error" in user_text:
                print(user_text)  # shows the error
            else:
                print("\nText from the file.")
                print(user_text[:200] + "...")  # showing a part of the text from the file

                # Language option
                language = input("\nChoose the language of the summary (English/Polish): ")
                if language not in ["English", "Polish"]:
                    language = "English"  # default language

                # Length option
                length = input("\nChoose the length of summary (short/detailed): ").lower()
                if length not in ["short", "detailed"]:
                    length = "short"  # default length

                # Summary generating
                summary = summarize_text(user_text, language, length)
                print("\nSummary:")
                print(summary)

                # File save option
                save_option = input("\nShould summary be saved to the file? (yes/no): ").lower()
                if save_option == "yes":
                    file_path = input("Enter the file name (ex. summary.txt): ")
                    save_summary_to_file(summary, file_path)

        elif option == "3":
            # Closing the program
            print("\nGood bye!")
            break
        else:
            print("\nWrong choice. Try again.")

if __name__ == "__main__":
    main()
