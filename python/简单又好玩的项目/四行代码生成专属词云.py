from wordcloud import WordCloud
cy = WordCloud()    # 创建词云对象
cy.generate('HuiXiaoYuan look forward to marking progress with you')  # 生成词云
cy.to_file('Sources/cy.png')    # 保存词云