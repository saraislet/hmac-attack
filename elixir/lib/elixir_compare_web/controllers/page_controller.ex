defmodule ElixirCompareWeb.PageController do
  use ElixirCompareWeb, :controller

  def index(conn, _params) do
    render conn, "index.html"
  end
end

defmodule ElixirCompareWeb.CompareController do
  use ElixirCompareWeb, :controller

  # def compare_strings(conn, %{"signature" => message_signature}) do
  def compare_strings(conn) do
    # IO.puts(message_signature)
    conn
    |> send_resp(200, "HELLO WORLD")
  end

end
