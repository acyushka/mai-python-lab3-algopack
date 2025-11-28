from src.dependencies.container import Container, get_container

import typer

app = typer.Typer(help="Algopack")

container: Container = get_container()


@app.command()
def fact(
        n: int = typer.Argument(..., help="Число, факториал которого ищем"),
        recursive: bool = typer.Option(False, "-r", "-R", help="Рекурсивный счет факториала"),
) -> None:
    try:
        if recursive:
            result = container.math_service.factorial_recursive(n)
        else:
            result = container.math_service.factorial(n)
        typer.echo(f"Факториал числа {n} = {result}")
    except Exception as e:
        typer.echo(f"Ошибка: {e}", err=True)


@app.command()
def fibo(
        n: int = typer.Argument(..., help="Номер числа Фибоначчи"),
        recursive: bool = typer.Option(False, "-r", "-R", help="Рекурсивный счет числа Фибоначчи"),
) -> None:
    try:
        if recursive:
            result = container.math_service.fibo_recursive(n)
        else:
            result = container.math_service.fibo(n)
        typer.echo(f"Фибоначчи от {n} = {result}")
    except Exception as e:
        typer.echo(f"Ошибка: {e}", err=True)


@app.command()
def bubble(a: list[int] = typer.Argument(..., help="Список целых чисел")):
    result = container.sorting.bubble_sort(a)
    typer.echo(f"Результат: {result}")


@app.command()
def quick(a: list[int] = typer.Argument(..., help="Список целых чисел")):
    result = container.sorting.quick_sort(a)
    typer.echo(f"Результат: {result}")


@app.command()
def counting(a: list[int] = typer.Argument(..., help="Список целых чисел")):
    result = container.sorting.counting_sort(a)
    typer.echo(f"Результат: {result}")


@app.command()
def heap(a: list[int] = typer.Argument(..., help="Список целых чисел")):
    result = container.sorting.heap_sort(a)
    typer.echo(f"Результат: {result}")


@app.command()
def radix(
        a: list[int] = typer.Argument(..., help="Список целых чисел"),
        base: int = typer.Option(10, "--base", "-b", help="Система счисления"),
) -> None:
    result = container.sorting.radix_sort(a, base)
    typer.echo(f"Результат: {result}")


@app.command()
def bucket(
        a: list[float] = typer.Argument(..., help="Список вещественных чисел"),
        buckets: int = typer.Option(None, "--buckets", "-b", help="Желаемое кол-во корзин"),
) -> None:
    result = container.sorting.bucket_sort(a, buckets)
    typer.echo(f"Результат: {result}")


@app.command()
def stack():
    stack = container.structure

    while True:
        try:
            stdin = typer.prompt("stack").strip()
            if not stdin:
                continue

            parts = stdin.split()
            command = parts[0].lower()

            match command:
                case "exit":
                    break
                case "quit":
                    break
                case "push":
                    try:
                        number = int(parts[1])
                        stack.push(number)
                        typer.echo(f"Успешный пуш {number}")
                    except Exception as e:
                        typer.echo(f"Ошибка: {e}")
                case "peek":
                    try:
                        output = stack.peek()
                        typer.echo(f"Самый верхний элемент: {output}")
                    except Exception as e:
                        typer.echo(f"Ошибка: {e}")
                case "pop":
                    try:
                        output = stack.pop()
                        typer.echo(f"Успешное извлечение верхнего элемента: {output}")
                    except Exception as e:
                        typer.echo(f"Ошибка: {e}")
                case "is_empty":
                    result = stack.is_empty()
                    if result is False:
                        typer.echo("Стек не пустой")
                    else:
                        typer.echo("Стек пустой")
                case "min":
                    try:
                        output = stack.min()
                        typer.echo(f"Текущий минимум в стеке: {output}")
                    except Exception as e:
                        typer.echo(f"Ошибка: {e}")
        except:
            typer.echo("Что-то пошло не так")
            break


@app.callback()
def main() -> None:
    pass


if __name__ == "__main__":
    app()
