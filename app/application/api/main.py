from fastapi import FastAPI


def create_app():
	return FastAPI(
		title="ConversationHub",
		docs_url="/api/docs",
		description="API for ConversationHub",
	)