
# APN Tester

[![st-badge]][apn-tester] [![MIT-badge]][MIT-url] [![black-badge]][black-url]

> test Apple Push Notification with ease

## Quick Start

### Use it Online

APN Tester on [Streamlit Community Cloud](https://apn-tester.streamlit.app)

### Install Locally

`pip install "httpx[http2]" cryptography pyjwt streamlit watchdog`

Then run it with [streamlit]

`streamlit run main.py`

### Work with Simulator

Edit the bundle ID and payloads in `simulator-payload.apns` then drag it to the simulator.

Or, edit `simulator.py` then run `python simulator.py`

## Motivation

### The Problem

- I need to send push notifications to test APNs (Apple Push Notification Service) for my iOS projects.
- Using push service providers like [Pusher](https://pusher.com) can be complicated. Typically, they require:
    - Installing and learning how to use their client library on both the iOS app and the server side.
    - Setting up a server to send push notifications.

### What I Want

- Avoid installing third-party libraries in my iOS project that would clutter the codebase.
- Avoid setting up a server just to send a few push notifications.
- Use a simple and user-friendly web UI to send push notifications easily - so here you go! 🚀

## Need Help?

[![git-logo] github issue][github issue]

[![x-logo] posts][x-post]

[apn-tester]: https://apn-tester.streamlit.app
[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-url]: https://github.com/psf/black
[git-logo]: https://api.iconify.design/bi/github.svg?color=%236FD886&width=20
[github issue]: https://github.com/hoishing/apn-tester/issues
[MIT-badge]: https://img.shields.io/github/license/hoishing/ptag
[MIT-url]: https://opensource.org/licenses/MIT
[st-badge]: https://static.streamlit.io/badges/streamlit_badge_black_white.svg
[streamlit]: https://docs.streamlit.io
[x-logo]: https://api.iconify.design/ri:twitter-x-fill.svg?width=20&color=DarkGray
[x-post]: https://x.com/hoishing
