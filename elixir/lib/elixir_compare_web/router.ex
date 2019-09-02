defmodule ElixirCompareWeb.Router do
  use ElixirCompareWeb, :router

  pipeline :browser do
    plug :accepts, ["html"]
    plug :fetch_session
    plug :fetch_flash
    plug :protect_from_forgery
    plug :put_secure_browser_headers
  end

  pipeline :api do
    # plug :fetch_query_params
    plug Api.ComparePlug
    plug :accepts, ["json"]
  end

  scope "/", ElixirCompareWeb do
    pipe_through :browser # Use the default browser stack

    get "/", PageController, :index
  end

  # Other scopes may use custom stacks.
  scope "/compare", ElixirCompareWeb do
    pipe_through :api

    get "/", CompareController, :compare_strings
  end
end
