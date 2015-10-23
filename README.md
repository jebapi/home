# home
Home for the JebApi Framework

## Description
JebApi (Java wEB API) is a web api framework modeled after Microsoft's ASP.NET Framework.
The idea is to take features from version 4 & 5 of ASP.NET and implement them in Java. 
Conceptualizing this framework has mostly come from developing with ASP.NET. Some details
as to how something works in ASP.NET has required directly looking at Mocrosoft's code. The
eventual goal of this is to have multiple libraries that can work together to provide
similar functionalities as ASP.NET with the power of a framework running behind the scenes.
This framework will start out small, but the goal is to take the following C# code:

```
[RoutePrefix("/api/todos")]
public class TodosController : Controller
{
  
  [HttpGet("/{id}")]
  public IActionResult Get(int id)
  {
    // fetch todo
    return Ok(todo);
  }
  
  [HttpPut("/{id}")]
  public IActionResult Put(int id, [FromBody] TodoModel model)
  {
    // update todo
    return Ok();
  }
  
}
```

In Java:

```
@RoutePrefix(route = "/api/todos")
public class TodosController : Controller {

  @HttpGet(route = "/{id}")
  public IHttpResult get(int id) {
    // fetch todo
    return Http.Ok(todo);
  }
  
  @HttpPut(route = "/{id}")
  public IHttpResult put(int id, @FromBody TodoModel model) {
    // update todo
    return Http.Ok();
  }
  
}
```

As you can see, it is almost syntactically the same, which is the point.
The goal is to allow the developer to focus on what is important, their
application; the data they serve. 

## Components
JebApi will consist of multiple libraries managed by a single framework.
To start, the following features will be developed as their own libraries
with their own repositories

1. [di] (https://github.com/jebapi/di) -- Dependency Injection
2. [routing] (https://github.com/jebapi/routing) -- routes requests to appropriate class and method
3. [annotations] (https://github.com/jebapi/annotations) -- contains annotations for specifying which class
      should be used for a route and which http method a class method
      is mapped to. Contains a parser to grab values from annotations
4. [http] (https://github.com/jebapi/http) -- wraps a socket connection and makes handling data coming in more
      elegantly

These will be the major components that will achieve the initial goal of
replicating some of the functionalities of ASP.NET in Java. Additional
components may come later, but these will be starter components.

## Misc.
Once a functional framework is available, templates with the proper libraries
will be available to clone and use for testing. There will be two templates.
One will be a fully contained template where the code that makes each part
work together the only external library. The other template will be a more
exposed template where access to what is under the hood is available. Some
components will be tightly coupled, but they will try and remain as independent
as possible.
