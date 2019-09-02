# This file is responsible for configuring your application
# and its dependencies with the aid of the Mix.Config module.
#
# This configuration file is loaded before any dependency and
# is restricted to this project.
use Mix.Config

# Configures the endpoint
config :elixir_compare, ElixirCompareWeb.Endpoint,
  url: [host: "localhost"],
  secret_key_base: "XCstpy8D0EVwjPATG2SLj1UdRM70Ftnj2P3ByXgU0/Br2W7YpS0OLq6Zj+kMaDWG",
  render_errors: [view: ElixirCompareWeb.ErrorView, accepts: ~w(html json)],
  pubsub: [name: ElixirCompare.PubSub,
           adapter: Phoenix.PubSub.PG2]

# Configures Elixir's Logger
config :logger, :console,
  format: "$time $metadata[$level] $message\n",
  metadata: [:user_id]

# Import environment specific config. This must remain at the bottom
# of this file so it overrides the configuration defined above.
import_config "#{Mix.env}.exs"
