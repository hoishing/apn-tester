import streamlit as st
from utils import create_payload, create_jwt_token, send_push_notification, EndPt
from textwrap import dedent

st.set_page_config(
    page_title="APNs Tester",
    page_icon=":material/mark_chat_unread:",
)

st.markdown(
    """
    ### :material/mark_chat_unread: &nbsp; Apple Push Notification Tester 

    > test Apple Push Notification with ease

    ![github](https://api.iconify.design/bi/github.svg?color=%236FD886&width=20) &nbsp;
    [source code](https://github.com/hoishing)
    """
)
st.write("")

# with st.form("my_form"):
st.write("#### APNs Configuration")

c1, c2 = st.columns(2)
bundle_id = c1.text_input("Bundle ID")
team_id = c2.text_input("Apple Team ID", placeholder="developer account team ID")

c3, c4 = st.columns(2)
key_id = c4.text_input(
    "APNs Key ID",
    placeholder="obtain from Apple Developer -> Certificates, IDs & Profiles -> Keys",
)
endpoint = c3.radio(
    "APNs Endpoint",
    options=EndPt.__args__,
    horizontal=True,
)

device_token = st.text_input(
    "Device Token",
    placeholder="obtain from application(_:didRegisterForRemoteNotificationsWithDeviceToken:)",
    help='snippet: `let pushToken = deviceToken.map { String(format: "%02.2hhx", $0) }.joined()`',
)
auth_key = st.text_area(
    "APNs Auth Key",
    placeholder=dedent(
        """\
        -----BEGIN PRIVATE KEY-----
        your private key data...
        -----END PRIVATE KEY-----
        """
    ),
    help="Copy and paste the content of your APNs Auth Key (.p8 file)",
)

st.write("#### Payload Content")
c5, c6 = st.columns(2)
title = c5.text_input("Title", placeholder="title message")
subtitle = c6.text_input("Subtitle", placeholder="subtitle message")
body = st.text_input("Body", placeholder="body message")
userInfo = st.text_input("userInfo", placeholder="any custom data")

# if st.form_submit_button("Send Push Notification"):
if st.button("Send Push Notification"):

    payload = create_payload(title, subtitle, body, userInfo)
    jwt_token = create_jwt_token(auth_key, team_id, key_id)
    response = send_push_notification(
        bundle_id, device_token, endpoint, payload, jwt_token
    )

    if response.status_code == 200:
        st.write("✅ Push notification sent ")
    else:
        st.write("⚠️ Failed to send push notification")
