from tavily import TavilyClient
from dotenv import load_dotenv
import os
from utils.scenario_inference_and_keyword_substitution import scenario_inference_and_keyword_substitution
from utils.split_input import split_input
from utils.analyze_question import analyze_question
load_dotenv()

# 查询
input = "Who is the most important princi in market economics and the most important indicator in financial sheet?"
input = scenario_inference_and_keyword_substitution(input)
questions = split_input(input)
keyword_list, domain_list = zip(*[analyze_question(question) for question in questions])
# 将元组转换为列表
keyword1_list = list(keyword_list) # ['principle', 'indicator']
keyword2_list = list(domain_list) # ['market economics', 'financial sheet']



# tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


# response = tavily_client.search(input_text)




# 基于哈希和语义的去重
# unique_results = []
# seen = set()
# for result in response['results']:
#     # 将字典转换为元组，以便进行哈希比较
#     result_tuple = tuple(sorted(result.items()))
#     if result_tuple not in seen:
#         seen.add(result_tuple)
#         unique_results.append(result)
# response['results'] = unique_results


# 打印查询结果
# print(response)
# print("\n查询内容:")
# print(response['query'])
# print("\n后续问题:")
# print(response['follow_up_questions'])
# print("\n答案:")
# print(response['answer'])
# print("\n查询结果:")
# for i, result in enumerate(response['results'], start=1):
#     print(f"  结果 {i}:")
#     print(f"    标题: {result['title']}")
#     print(f"    链接: {result['url']}")
#     print(f"    内容: {result['content']}")
#     print(f"    得分: {result['score']}")
#     print(f"    原始内容: {result['raw_content']}")
# print("\n响应时间:")
# print(response['response_time'])