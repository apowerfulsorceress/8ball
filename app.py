if st.button("Consult the Oracle"):
    if name and question:
        st.write("The incense swirls... the shadows gather...")
        answer = random.choice(responses)
        st.success(f"{name}, the Oracle reveals: *{answer}*")

        # 📝 Send to Google Form
        form_url = "https://docs.google.com/forms/d/e/1FAIpQLSdEYgJt63t5-xrMBWNASkWKYoZ1UzXwakZX_zyMIe7oD12vbw/formResponse"
        form_data = {
            "entry.1171538699": name,
            "entry.1310975289": question,
            "entry.1930830611": answer
        }
        try:
            requests.post(form_url, data=form_data)
        except:
            st.warning("Could not log question to Oracle log—but the spirits heard you.")
    else:
        st.warning("You must offer both your name and a question.")
