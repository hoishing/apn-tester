
# Apple Push Notification Tester

[![MIT-badge]][MIT-url] [![black-badge]][black-url]

> test push notification with ease

## Quick Start

### Use it on Streamlit Community Cloud

<https://apn-tester.streamlit.app>

### Local Development

`pip install "httpx[http2]" cryptography pyjwt streamlit watchdog`

then run [streamlit]

`streamlit run main.py`

### Using Simulator

edit `simulator-payload.apns` then drag it to the simulator

or, edit `simulator.py` then run `python simulator.py`

## Need Help?

[![git-logo] github issue][github issue]

[![x-logo] posts][x-post]

[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-url]: https://github.com/psf/black
[git-logo]: https://api.iconify.design/bi/github.svg?color=%236FD886&width=20
[github issue]: https://github.com/hoishing/apn-tester/issues
[MIT-badge]: https://img.shields.io/github/license/hoishing/ptag
[MIT-url]: https://opensource.org/licenses/MIT
[x-logo]: https://api.iconify.design/ri:twitter-x-fill.svg?width=20&color=DarkGray
[x-post]: https://x.com/hoishing
[streamlit]: https://docs.streamlit.io
