import asyncio

from dotenv import load_dotenv

load_dotenv()


async def main():
    print("=" * 60)
    print("Enterprise Operations Assistant")
    print("=" * 60)

    print("Host started successfully.")


if __name__ == "__main__":
    asyncio.run(main())