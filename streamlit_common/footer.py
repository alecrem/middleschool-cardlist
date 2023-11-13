import streamlit as st

fa_import = """
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
"""
x_icon = '<i class="fa-brands fa-x-twitter" style="color: #ffffff;"></i>'
x_url = "https://x.com/KarawapoM"
gh_icon = '<i class="fa-brands fa-github" style="color: #ffffff;"></i>'
gh_url = "https://github.com/alecrem/middleschool-tutor/"


def write_header():
    st.write(fa_import, unsafe_allow_html=True)


def write_footer():
    st.write(
        """
    ---

    Portions of Middle School Tutor are unofficial Fan Content permitted under the Wizards of the Coast Fan Content Policy. The literal and graphical information presented on this site about Magic: The Gathering, including card images, mana symbols, and Oracle text, is copyright Wizards of the Coast, LLC, a subsidiary of Hasbro, Inc.

    Middle School Tutor is not produced by or endorsed by Wizards of the Coast. The GitHub and Twitter logos are copyright their respective owners. Middle School Tutor is not produced by or endorsed by these services.
    """
    )
    write_header()
    st.write(
        f"### [{x_icon}]({x_url})&nbsp;&nbsp;[{gh_icon}]({gh_url})",
        unsafe_allow_html=True,
    )
    st.write("##### All other content MIT licensed since 2022 by alecrem.")
