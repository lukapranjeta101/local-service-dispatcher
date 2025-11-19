from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from service_sources import get_service_list, get_service_details

app = FastAPI(
    title="Local Service Dispatcher API",
    version="1.0.0",
    description="Provides local service provider search, details, and booking assistance."
)

# ---------- CORS (Required for ChatGPT + Railway) ----------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- ROOT ROUTE (Required for Railway) ----------

@app.get("/")
def root():
    return {"status": "Local Service Dispatcher API is running!"}

# ---------- MODELS ----------

class SearchRequest(BaseModel):
    location: str
    service_type: str


class Provider(BaseModel):
    id: str
    name: str
    rating: float
    price_level: str
    phone: str
    address: str
    availability: str


class ProviderList(BaseModel):
    providers: List[Provider]


class DetailRequest(BaseModel):
    provider_id: str


class ProviderDetail(BaseModel):
    id: str
    name: str
    description: str
    services: List[str]
    rating: float
    phone: str
    address: str
    availability: str


# ---------- ROUTES ----------

@app.post("/search", response_model=ProviderList)
def search_services(req: SearchRequest):
    results = get_service_list(req.location, req.service_type)
    return {"providers": results}


@app.post("/details", response_model=ProviderDetail)
def provider_details(req: DetailRequest):
    details = get_service_details(req.provider_id)
    return details
