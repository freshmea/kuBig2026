namespace HelloLibrary;

public sealed class HelloService
{
    private readonly string _name;

    public HelloService(string name)
    {
        _name = name;
    }

    public string Greet()
    {
        return $"hello, {_name} from .NET!";
    }

    public static int Add(int left, int right)
    {
        return left + right;
    }
}
