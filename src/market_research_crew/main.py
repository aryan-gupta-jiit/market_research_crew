# #!/usr/bin/env python
# import sys
# import warnings

# from datetime import datetime

# from market_research_crew.crew import MarketResearchCrew

# warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# def run():
#     """
#     Run the crew.
#     """
#     inputs = {
#         "product_idea": "An AI powered tool that summarizes youtube videos on my channel and posts the summary on various social media platforms like LinkedIn, Instagram, Facebook,X, WhatsApp",
#     }

#     try:
#         MarketResearchCrew().crew().kickoff(inputs=inputs)
#     except Exception as e:
#         raise Exception(f"An error occurred while running the crew: {e}")

#!/usr/bin/env python
import sys
import warnings
from datetime import datetime

from market_research_crew.crew import MarketResearchCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        "product_idea": "An AI powered tool that summarizes youtube videos on my channel and posts the summary on various social media platforms like LinkedIn, Instagram, Facebook,X, WhatsApp",
    }

    print(f"\n📅 Started at: {datetime.now()}")
    print(f"🎯 Product Idea: {inputs['product_idea'][:100]}...")
    
    try:
        # Get the crew and run it
        crew = MarketResearchCrew().crew()
        print("🚀 Starting crew execution...")
        
        result = crew.kickoff(inputs=inputs)
        
        print(f"\n" + "="*60)
        print(f"✅ CREW EXECUTION COMPLETE!")
        print(f"📅 Finished at: {datetime.now()}")
        print(f"📄 Output saved to: reports/market_research_report.md")
        print("="*60)
        
        # Show a preview of the result
        if result:
            print(f"\n📝 Result preview (first 500 chars):")
            print("-"*40)
            print(str(result)[:500] + "...")
            print("-"*40)
        
    except Exception as e:
        print(f"\n❌ Error during execution: {e}")
        import traceback
        traceback.print_exc()
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    run()