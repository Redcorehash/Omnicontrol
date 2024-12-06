# Hugging Face Space Interaction with Yuanshi/OminiControl

This repository contains a Python script to interact with the Hugging Face Space `https://huggingface.co/spaces/Yuanshi/OminiControl`. The script uses the Hugging Face API to send requests and receive responses from the model hosted on the Space.

## Overview

The Hugging Face Space `Yuanshi/OminiControl` is a hosted model that can be interacted with via API requests. This repository provides a simple Python script to demonstrate how to send requests to the Space and process the responses.

![OmniControl Interface](images/omni_control_interface.png)

*Figure 1: Interface of the OmniControl Space*

## Prerequisites

Before you can use the script, you need to have the following:

- A Hugging Face account and an API token. You can get your API token from your [Hugging Face account settings](https://huggingface.co/settings/tokens).
- Python 3.x installed on your machine.
- The `requests` library installed. You can install it using pip:

  ```bash
  pip install requests
