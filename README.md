# Telegram GPT assistant

## Overview
This is a Telegram chat bot integrated with GPT to engage in natural language conversations with users. The chat bot uses OpenAI's GPT model to generate human-like responses to user queries, making it a versatile and interactive AI-powered bot.
Based on [gpt_assistant_lib](https://github.com/elisey/gpt_assistant_lib) library


## How to run

Create .env file

```shell
cp .env.example .env
vim .env
```

Build docker image and run it

```shell
task build
task run
```

How to check logs

```shell
task logs
```

Stop and remove container

```shell
task stop
task remove
```

## Contributing

Format code

```shell
task format
```

Run linters

```shell
task lint
```