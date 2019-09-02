defmodule Api.ComparePlug do
  @behaviour Plug
  require Logger

  import Plug.Conn

  def init(options), do: options

  def call(conn, _opts) do
    verify_signature(conn)
    |> send_response(conn)
  end

  def verify_signature(_conn) do
    nonconstant_compare("hello", "hello")
  end

  defp nonconstant_compare(target, guess) when target == guess, do: :ok

  defp nonconstant_compare(_target, _guess), do: :error

  defp send_response(:ok, conn), do: conn
  defp send_response(:error, conn), do:
    conn
    |> send_resp(403, "Error checking signature")
    |> halt()
end
