# import os
# import sys
# import warnings

# # COMPLETELY BLOCK LiteLLM proxy imports
# # os.environ['LITELLM_LOG'] = 'OFF'
# # os.environ['LITELLM_LOG'] = 'true'
# os.environ['LITELLM_LOG'] = 'ERROR'

# from crewai import Agent, Crew, Process, Task, LLM
# from crewai.project import CrewBase, agent, crew, task
# from crewai.agents.agent_builder.base_agent import BaseAgent
# from typing import List
# from crewai_tools import SerperDevTool, ScrapeWebsiteTool, SeleniumScrapingTool
# from dotenv import load_dotenv

# load_dotenv()

# # Use the EXACT format that works - based on your Ollama output
# local_llm = LLM(
#     model="ollama/mistral",  # This format usually works with CrewAI
#     temperature=0.2,
#     base_url="http://localhost:11434",
#     request_timeout=2400
# )

# # Test it immediately
# print("Testing LLM...")
# try:
#     result = local_llm.call(messages=[{"role": "user", "content": "Hello"}])
#     print(f"✅ LLM test passed: {result[:50]}...")
# except Exception as e:
#     print(f"❌ LLM test failed: {e}")
#     print("Trying alternative format...")
    
#     # Alternative format
#     local_llm = LLM(
#         model="ollama/mistral:latest",  # Include :latest
#         temperature=0.2,
#         base_url="http://localhost:11434",
#         request_timeout=2400
#     )

# # create the tools for the agent
# web_search_tool = SerperDevTool()
# web_scraping_tool = ScrapeWebsiteTool()
# selenium_scraping_tool = SeleniumScrapingTool()

# toolkit = [web_search_tool, web_scraping_tool, selenium_scraping_tool]


# @CrewBase
# class MarketResearchCrew():
#     """MarketResearchCrew crew"""

#     agents: List[BaseAgent]
#     tasks: List[Task]

#     # provide the path for configuration files
#     agents_config="config/agents.yaml"
#     tasks_config="config/tasks.yaml"

#     # =========== Agents ===========

#     @agent
#     def market_research_specialist(self) -> Agent:
#         return Agent(
#             config=self.agents_config["market_research_specialist"],
#             llm=local_llm,
#             tools=toolkit,
#             verbose=False
#         )
    
#     # @agent
#     # def competitive_intelligence_analyst(self) -> Agent:
#     #     return Agent(
#     #         config=self.agents_config["competitive_intelligence_analyst"],
#     #         llm=local_llm,
#     #         tools=toolkit,
#     #         verbose=False
#     #     )
        
#     # @agent
#     # def customer_insights_researcher(self) -> Agent:
#     #     return Agent(
#     #         config=self.agents_config["customer_insights_researcher"],
#     #         llm=local_llm,
#     #         tools=toolkit,
#     #         verbose=False
#     #     )
        
#     # @agent
#     # def product_strategy_advisor(self) -> Agent:
#     #     return Agent(
#     #         config=self.agents_config["product_strategy_advisor"],
#     #         llm=local_llm,
#     #         tools=toolkit,
#     #         verbose=False
#     #     )
        
#     # @agent
#     # def business_analyst(self) -> Agent:
#     #     return Agent(
#     #         config=self.agents_config["business_analyst"],
#     #         llm=local_llm,
#     #         tools=toolkit,
#     #         verbose=False
#     #     )
    
#     # =========== Tasks ===========
#     @task
#     def market_research_task(self) -> Task:
#         return Task(
#             config=self.tasks_config["market_research_task"]
#         )
        
#     # @task
#     # def competitive_intelligence_task(self) -> Task:
#     #     return Task(
#     #         config=self.tasks_config["competitive_intelligence_task"],
#     #         context=[self.market_research_task()]
#     #     )
        
#     # @task
#     # def customer_insights_task(self) -> Task:
#     #     return Task(
#     #         config=self.tasks_config["customer_insights_task"],
#     #         context=[self.market_research_task(),
#     #                  self.competitive_intelligence_task()]
#     #     )
        
#     # @task
#     # def product_strategy_task(self) -> Task:
#     #     return Task(
#     #         config=self.tasks_config["product_strategy_task"],
#     #         context=[self.market_research_task(),
#     #                  self.competitive_intelligence_task(),
#     #                  self.customer_insights_task()]
#     #     )
        
#     # @task
#     # def business_analyst_task(self) -> Task:
#     #     return Task(
#     #         config=self.tasks_config["business_analyst_task"],
#     #         context=[self.market_research_task(),
#     #                  self.competitive_intelligence_task(),
#     #                  self.customer_insights_task(),
#     #                  self.product_strategy_task()],
#     #         output_file="reports/report.md"
#     #     )
        
#     # ================= Crew ===========================
    
#     @crew
#     def crew(self) -> Crew:
#         return Crew(
#             agents=self.agents,
#             tasks=self.tasks,
#             process=Process.sequential
#         )

import os
import sys
import warnings

# COMPLETELY BLOCK LiteLLM proxy imports
os.environ['LITELLM_LOG'] = 'ERROR'

from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, SeleniumScrapingTool
from dotenv import load_dotenv

load_dotenv()

print("=" * 60)
print("🚀 MARKET RESEARCH CREW - STARTING")
print("=" * 60)

# Use the EXACT format that works - based on your Ollama output
local_llm = LLM(
    model="ollama/llama3.2:3b",  # This format usually works with CrewAI
    temperature=0.2,
    base_url="http://localhost:11434",
    request_timeout=3600,  # Reduced from 2400 to 5 minutes
    # max_tokens=512  # Limit response size
)

# Test it immediately
print("🧪 Testing LLM...")
try:
    result = local_llm.call(messages=[{"role": "user", "content": "Say READY in one word"}])
    print(f"✅ LLM test passed: {result}")
except Exception as e:
    print(f"❌ LLM test failed: {e}")
    print("Trying alternative format...")
    
    # Alternative format
    local_llm = LLM(
        model="ollama/llama3.2:3b",  # Include :latest
        temperature=0.2,
        base_url="http://localhost:11434",
        request_timeout=3600,
        # max_tokens=512
    )

# create the tools for the agent
web_search_tool = SerperDevTool()
web_scraping_tool = ScrapeWebsiteTool()
# selenium_scraping_tool = SeleniumScrapingTool()

# toolkit = [web_search_tool, web_scraping_tool, selenium_scraping_tool]
toolkit = [web_search_tool, web_scraping_tool]

print("🛠️  Tools configured")

@CrewBase
class MarketResearchCrew():
    """MarketResearchCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # provide the path for configuration files
    agents_config="config/agents.yaml"
    tasks_config="config/tasks.yaml"

    # =========== Agents ===========
    @agent
    def market_research_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["market_research_specialist"],
            llm=local_llm,
            tools=toolkit,
            verbose=True,  # CHANGED TO TRUE - see agent thinking
            max_iter=3,
            max_execution_time=3600,
            max_rpm=3  # Limit requests per minute
        )
    
    @agent
    def competitive_intelligence_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["competitive_intelligence_analyst"],
            llm=local_llm,
            tools=toolkit,
            verbose=True,  # CHANGED TO TRUE - see agent thinking
            max_iter=3,
            max_execution_time=3600,
            max_rpm=3  # Limit requests per minute
        )
        
    @agent
    def customer_insights_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["customer_insights_researcher"],
            llm=local_llm,
            tools=toolkit,
            verbose=True,  # CHANGED TO TRUE - see agent thinking
            max_iter=3,
            max_execution_time=3600,
            max_rpm=3  # Limit requests per minute
        )
        
    @agent
    def product_strategy_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config["product_strategy_advisor"],
            llm=local_llm,
            tools=toolkit,
            verbose=True,  # CHANGED TO TRUE - see agent thinking
            max_iter=3,
            max_execution_time=3600,
            max_rpm=3  # Limit requests per minute
        )
        
    @agent
    def business_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["business_analyst"],
            llm=local_llm,
            tools=toolkit,
            verbose=True,  # CHANGED TO TRUE - see agent thinking
            max_iter=3,
            max_execution_time=3600,
            max_rpm=3  # Limit requests per minute
        )
    
# =========== Tasks ===========
    @task
    def market_research_task(self) -> Task:
        return Task(
            config=self.tasks_config["market_research_task"]
        )
        
    @task
    def competitive_intelligence_task(self) -> Task:
        return Task(
            config=self.tasks_config["competitive_intelligence_task"],
            context=[self.market_research_task()]
        )
        
    @task
    def customer_insights_task(self) -> Task:
        return Task(
            config=self.tasks_config["customer_insights_task"],
            context=[self.market_research_task(),
                     self.competitive_intelligence_task()]
        )
        
    @task
    def product_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config["product_strategy_task"],
            context=[self.market_research_task(),
                     self.competitive_intelligence_task(),
                     self.customer_insights_task()]
        )
        
    @task
    def business_analyst_task(self) -> Task:
        return Task(
            config=self.tasks_config["business_analyst_task"],
            context=[self.market_research_task(),
                     self.competitive_intelligence_task(),
                     self.customer_insights_task(),
                     self.product_strategy_task()],
            output_file="reports/report.md"
        )
    
    # =========== Tasks ===========
    # @task
    # def market_research_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config["market_research_task"],
    #         agent=self.market_research_specialist(),  # Explicitly set agent
    #         output_file="reports/market_research_report.md"  # ADDED output file
    #     )
        
    # ================= Crew ===========================
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True  # CHANGED TO 2 - show crew execution
        )

print("✅ Crew setup complete")
print("📄 Output will be saved to: reports/market_research_report.md")
print("🎯 Starting execution...")
print("=" * 60)