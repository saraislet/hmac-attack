defmodule ElixirCompare do
  use Bitwise
  
  def nonconstant_compare(target, guess) when target == guess, do: :ok

  def nonconstant_compare(_target, _guess), do: :error

  def repeat_compare(target, guess, count) when count<=1 do
    nonconstant_compare(target, guess)
  end

  def repeat_compare(target, guess, count) do
    nonconstant_compare(target, guess)
    repeat_compare(target, guess, count - 1)
  end

  def constant_time_compare(a, b) do
    constant_time_compare(a, b, 0)
  end

  def constant_time_compare(<<firsta, resta::binary>>, <<firstb, restb::binary>>, diff) do
    constant_time_compare(resta, restb, diff ||| (firsta ^^^ firstb))
  end

  def constant_time_compare(<<>>, <<>>, diff) do
    diff == 0
  end

end
