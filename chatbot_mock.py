import streamlit as st
import spacy

nlp = spacy.load("ja_core_news_sm")

faq_data = [
    {
        "category": "社有車利用",
        "questions": ["社有車の使い方がわからない", "社用車の借り方"],
        "answer": "グループウエアから予約＞台帳記入＞アルコールチェック＞乗車前点検"
    },
    {
        "category": "グループウエア",
        "questions": ["グループウエア 初期ログインIDPWがわからない", "グループウェア ログイン情報"],
        "answer": "IDは社員番号 PWも社員番号"
    },
    {
        "category": "教育用アプリ",
        "questions": ["教育用アプリ ログイン失敗", "アプリにログインできない"],
        "answer": "会社コードを確認"
    }
]

def find_answer_spacy(user_input, faq_data):
    doc_user = nlp(user_input)
    for item in faq_data:
        for question in item["questions"]:
            doc_question = nlp(question)
            common_tokens = 0
            for token_user in doc_user:
                for token_question in doc_question:
                    if token_user.lemma_ == token_question.lemma_:
                        common_tokens += 1
            if common_tokens > 0 and len(doc_user) > 0 and common_tokens / len(doc_user) > 0.5:
                return item["answer"]
    return "ご質問の意味がよくわかりません。別の表現でお試しください。"

st.title("AIチャットボット モックアップ")

user_input = st.text_input("質問を入力してください:")

if user_input:
    answer = find_answer_spacy(user_input, faq_data)
    st.write("回答:", answer)