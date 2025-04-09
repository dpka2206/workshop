from datetime import datetime
from trip_planner.crew import TripPlanner
from langchain_google_genai import ChatGoogleGenerativeAI
import browser_use
import asyncio


def run():
    print("Welcome to the Trip Planner!")

    try:
        destination = input("Enter your destination: ")
        no_of_days = input("How many days is your trip? ")
        no_of_people = input("How many people are going? ")
        budget = input("Enter your total budget (e.g., $10000): ")
        interests = input(
            "What are your interests? (e.g., lakeside views, hiking, etc.): "
        )
        city = input("Enter your city: ")

        inputs = {
            "destination": destination,
            "date": f"{datetime.now().year}-{datetime.now().month}-{datetime.now().day}",
            "no_of_days": no_of_days,
            "no_of_people": no_of_people,
            "budget": budget,
            "interests": interests,
            "city": city,
        }

        TripPlanner().crew().kickoff(inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


llm = ChatGoogleGenerativeAI(
                model="gemini-2.0-flash",
                api_key="AIzaSyCMTL1rozzOgXo-Ro-L4nqU964o8tB3bRY")



browser = browser_use.Browser(
    config=browser_use.BrowserConfig(
        chrome_instance_path='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
    )
)

def get_browser_agent(tasks):
    async def main(tasks):
        agent = browser_use.Agent(
            task=tasks,
            llm=llm,
            browser=browser
        )
        result = await agent.run()
        await browser.close()
        with open("output/output.txt", "w", encoding="utf-8") as f:
            f.write(str(result))

    asyncio.run(main(tasks))


if __name__ == "__main__":
    # run()
    with open("prompt/flights.txt", "r") as file:
        task = file.read()
    get_browser_agent(task)