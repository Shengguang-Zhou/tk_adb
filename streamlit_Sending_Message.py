from pipeline_sending_msg import *

st.title('Sending Message Datatable')

def csv_to_list_pandas(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    return df.iloc[:, 0].tolist()

test_list = csv_to_list_pandas('/Users/shengguang/PycharmProjects/TikTok/data/message_list.csv')

# name_used = st.text_input('What\'s your name?')
if st.button('执行私信'):
    test_table = send_private_msg(test_list,'Jeremy')
    st.table(test_table)

if st.button('执行评论'):
    test_table = send_comment_known_id(test_list)
    st.table(test_table)



