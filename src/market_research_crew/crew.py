import os
import sys
import warnings

# COMPLETELY BLOCK LiteLLM proxy imports
# os.environ['LITELLM_LOG'] = 'OFF'
# os.environ['LITELLM_LOG'] = 'true'
os.environ['LITELLM_LOG'] = 'ERROR'

from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, SeleniumScrapingTool
from dotenv import load_dotenv

load_dotenv()

# Use the EXACT format that works - based on your Ollama output
local_llm = LLM(
    model="ollama/mistral",  # This format usually works with CrewAI
    temperature=0.2,
    base_url="http://localhost:11434",
    request_timeout=2400
)

# Test it immediately
print("Testing LLM...")
try:
    result = local_llm.call(messages=[{"role": "user", "content": "Hello"}])
    print(f"✅ LLM test passed: {result[:50]}...")
except Exception as e:
    print(f"❌ LLM test failed: {e}")
    print("Trying alternative format...")
    
    # Alternative format
    local_llm = LLM(
        model="ollama/mistral:latest",  # Include :latest
        temperature=0.2,
        base_url="http://localhost:11434",
        request_timeout=2400
    )

# create the tools for the agent
web_search_tool = SerperDevTool()
web_scraping_tool = ScrapeWebsiteTool()
selenium_scraping_tool = SeleniumScrapingTool()

toolkit = [web_search_tool, web_scraping_tool, selenium_scraping_tool]


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
            verbose=False
        )
    
    # @agent
    # def competitive_intelligence_analyst(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config["competitive_intelligence_analyst"],
    #         llm=local_llm,
    #         tools=toolkit,
    #         verbose=False
    #     )
        
    # @agent
    # def customer_insights_researcher(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config["customer_insights_researcher"],
    #         llm=local_llm,
    #         tools=toolkit,
    #         verbose=False
    #     )
        
    # @agent
    # def product_strategy_advisor(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config["product_strategy_advisor"],
    #         llm=local_llm,
    #         tools=toolkit,
    #         verbose=False
    #     )
        
    # @agent
    # def business_analyst(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config["business_analyst"],
    #         llm=local_llm,
    #         tools=toolkit,
    #         verbose=False
    #     )
    
    # =========== Tasks ===========
    @task
    def market_research_task(self) -> Task:
        return Task(
            config=self.tasks_config["market_research_task"]
        )
        
    # @task
    # def competitive_intelligence_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config["competitive_intelligence_task"],
    #         context=[self.market_research_task()]
    #     )
        
    # @task
    # def customer_insights_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config["customer_insights_task"],
    #         context=[self.market_research_task(),
    #                  self.competitive_intelligence_task()]
    #     )
        
    # @task
    # def product_strategy_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config["product_strategy_task"],
    #         context=[self.market_research_task(),
    #                  self.competitive_intelligence_task(),
    #                  self.customer_insights_task()]
    #     )
        
    # @task
    # def business_analyst_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config["business_analyst_task"],
    #         context=[self.market_research_task(),
    #                  self.competitive_intelligence_task(),
    #                  self.customer_insights_task(),
    #                  self.product_strategy_task()],
    #         output_file="reports/report.md"
    #     )
        
    # ================= Crew ===========================
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential
        )

# from crewai import Agent, Crew, Process, Task
# from crewai.project import CrewBase, agent, crew, task
# from crewai_tools import SerperDevTool
# from dotenv import load_dotenv
# from crewai import LLM
# import os

# load_dotenv()

# # ===== LLMs =====

# llm_agents = LLM(
#     model="groq/llama-3.1-8b-instant",
#     api_key=os.getenv("GROQ_API_KEY"),
#     max_tokens=512,
#     temperature=0.2
# )

# llm_final = LLM(
#     model="gemini/gemini-2.5-flash",
#     api_key=os.getenv("GEMINI_API_KEY"),
#     max_tokens=800,
#     temperature=0.3
# )

# # ===== Tools =====
# web_search_tool = SerperDevTool()

# @CrewBase
# class MarketResearchCrew:
#     agents_config = "config/agents.yaml"
#     tasks_config = "config/tasks.yaml"

#     # ========== AGENTS ==========

#     @agent
#     def market_research_specialist(self) -> Agent:
#         return Agent(
#             config=self.agents_config["market_research_specialist"],
#             llm=llm_agents,
#             tools=[web_search_tool],
#             verbose=False
#         )

#     @agent
#     def competitive_intelligence_analyst(self) -> Agent:
#         return Agent(
#             config=self.agents_config["competitive_intelligence_analyst"],
#             llm=llm_agents,
#             tools=[web_search_tool],
#             verbose=False
#         )

#     @agent
#     def customer_insights_researcher(self) -> Agent:
#         return Agent(
#             config=self.agents_config["customer_insights_researcher"],
#             llm=llm_agents,
#             tools=[web_search_tool],
#             verbose=False
#         )

#     @agent
#     def product_strategy_advisor(self) -> Agent:
#         return Agent(
#             config=self.agents_config["product_strategy_advisor"],
#             llm=llm_agents,
#             verbose=False
#         )

#     @agent
#     def business_analyst(self) -> Agent:
#         return Agent(
#             config=self.agents_config["business_analyst"],
#             llm=llm_final,
#             verbose=False
#         )

#     # ========== TASKS ==========

#     @task
#     def market_research_task(self) -> Task:
#         return Task(config=self.tasks_config["market_research_task"])

#     @task
#     def competitive_intelligence_task(self) -> Task:
#         return Task(config=self.tasks_config["competitive_intelligence_task"])

#     @task
#     def customer_insights_task(self) -> Task:
#         return Task(config=self.tasks_config["customer_insights_task"])

#     @task
#     def product_strategy_task(self) -> Task:
#         return Task(config=self.tasks_config["product_strategy_task"])

#     @task
#     def business_analyst_task(self) -> Task:
#         return Task(
#             config=self.tasks_config["business_analyst_task"],
#             output_file="reports/report.md"
#         )

#     # ========== CREW ==========

#     @crew
#     def crew(self) -> Crew:
#         return Crew(
#             agents=self.agents,
#             tasks=self.tasks,
#             process=Process.sequential
#         )
