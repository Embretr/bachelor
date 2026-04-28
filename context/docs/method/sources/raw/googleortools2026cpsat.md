# Constraint Optimization

**Constraint optimization** , or
[**constraint programming**](https://en.wikipedia.org/wiki/Constraint_programming)
(CP), is the name given to identifying feasible solutions out of a very large
set of candidates, where the problem can be modeled in terms of arbitrary
constraints.
CP problems arise in many scientific and engineering disciplines. (The word
"programming" is a bit of a misnomer, similar to how "computer" once meant
"a person who computes". Here, "programming" refers to the arrangement of a plan
, rather than programming in a computer language.)

CP is based on *feasibility* (finding a feasible solution) rather than
optimization (finding an optimal solution) and focuses on the constraints and
variables rather than the objective function. In fact, a CP problem may not even
have an objective function --- the goal may be to narrow down a very
large set of possible solutions to a more manageable subset by adding
constraints to the problem.

An example of a problem that is well-suited for CP is **employee scheduling** .
The problem arises when companies that operate continuously --- such as
factories --- need to create weekly schedules for their employees. Here's a
very simplified example: a company runs three 8-hour shifts per day and assigns
three of its four employees to different shifts each day, while giving the
fourth the day off. Even in such a small case, the number of possible schedules
is huge: each day, there are `4! = 4 * 3 * 2 * 1 = 24` possible employee
assignments, so the number of possible weekly schedules is 24^7^, which
is over 4.5 billion.
Usually there will be other constraints that reduce the number of feasible
solutions --- for example, that each employee works at least a minimum
number of days per week. The CP method keeps track of which solutions remain
feasible when you add new constraints, which makes it a powerful tool for
solving large, real-world scheduling problems.

CP has a widespread and very active community around the world with dedicated
scientific journals, conferences, and an arsenal of different solving techniques
. CP has been successfully applied in planning, scheduling, and numerous other
domains with heterogeneous constraints.

## Tools

Google provides few ways to solve problems:

- [CP-SAT solver](https://developers.google.com/optimization/cp/cp_solver): A **constraint programming** solver that uses SAT (satisfiability) methods.
- [Original CP solver](https://developers.google.com/optimization/routing/original_cp_solver): A **constraint programming** solver used in the routing library.

If your problem can be modeled with a linear objective and linear constraints,
then you have a [linear programming](https://developers.google.com/optimization/lp) problem and should
consider [MPSolver](https://developers.google.com/optimization/lp/mpsolver). (However, routing problems are
typically best solved with our [vehicle routing library](https://developers.google.com/optimization/routing)
even if they can be represented with a linear model.)

## Examples

The [next section](https://developers.google.com/optimization/cp/cp_solver) describes the CP-SAT solver, the
primary OR-Tools solver for constraint programming. (SAT stands for
**satisfiability**: the solver uses techniques for solving SAT problems along
with CP methods.)

Here are some examples of scheduling problems that are well-suited for the
CP-SAT solver:

- [Employee Scheduling](https://developers.google.com/optimization/scheduling/employee_scheduling)
- [The Job shop problem](https://developers.google.com/optimization/scheduling/job_shop)

Two classic CP problems are the [N-queens problem](https://developers.google.com/optimization/cp/queens) and
[cryptarithmetic puzzles](https://developers.google.com/optimization/puzzles/cryptarithmetic).

*[CP]: Constraint Programming

# Employee Scheduling

Organizations whose employees work multiple shifts need to schedule sufficient
workers for each daily shift. Typically, the schedules will have constraints,
such as "no employee should work two shifts in a row". Finding a schedule that
satisfies all constraints can be computationally difficult.

The following sections present two examples of employee scheduling problems, and
show how to solve them using the [CP-SAT solver](https://developers.google.com/optimization/cp/cp_solver).

For a more sophisticated example, see this
[shift scheduling program](https://github.com/google/or-tools/blob/main/examples/python/shift_scheduling_sat.py)
on GitHub.

> [!NOTE]
> Google's [Operations Research
> API](https://developers.google.com/optimization/service) provides a free [workforce scheduling
> service](https://developers.google.com/optimization/service/reference/rest/v1/scheduling) for solving many common problems.

## A nurse scheduling problem

In the next example, a hospital supervisor needs to create a schedule for four
nurses over a three-day period, subject to the following conditions:

- Each day is divided into three 8-hour shifts.
- Every day, each shift is assigned to a single nurse, and no nurse works more than one shift.
- Each nurse is assigned to at least two shifts during the three-day period.

The following sections present a solution to the nurse scheduling problem.

### Import the libraries

The following code imports the required library.

### Python

```python
from ortools.sat.python import cp_model
```

### C++

```c++
#include <stdlib.h>

#include <atomic>
#include <map>
#include <numeric>
#include <string>
#include <tuple>
#include <vector>

#include "absl/base/log_severity.h"
#include "absl/log/globals.h"
#include "absl/strings/str_format.h"
#include "ortools/base/init_google.h"
#include "ortools/base/logging.h"
#include "ortools/sat/cp_model.h"
#include "ortools/sat/cp_model.pb.h"
#include "ortools/sat/cp_model_solver.h"
#include "ortools/sat/model.h"
#include "ortools/sat/sat_parameters.pb.h"
#include "ortools/util/time_limit.h"
```

### Java

```java
import com.google.ortools.Loader;
import com.google.ortools.sat.CpModel;
import com.google.ortools.sat.CpSolver;
import com.google.ortools.sat.CpSolverSolutionCallback;
import com.google.ortools.sat.CpSolverStatus;
import com.google.ortools.sat.LinearExpr;
import com.google.ortools.sat.LinearExprBuilder;
import com.google.ortools.sat.Literal;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.IntStream;
```

### C#

```c#
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using Google.OrTools.Sat;
```

### Data for the example

The following code creates the data for the example.

### Python

```python
num_nurses = 4
num_shifts = 3
num_days = 3
all_nurses = range(num_nurses)
all_shifts = range(num_shifts)
all_days = range(num_days)
```

### C++

```c++
const int num_nurses = 4;
const int num_shifts = 3;
const int num_days = 3;

std::vector<int> all_nurses(num_nurses);
std::iota(all_nurses.begin(), all_nurses.end(), 0);

std::vector<int> all_shifts(num_shifts);
std::iota(all_shifts.begin(), all_shifts.end(), 0);

std::vector<int> all_days(num_days);
std::iota(all_days.begin(), all_days.end(), 0);
```

### Java

```java
final int numNurses = 4;
final int numDays = 3;
final int numShifts = 3;

final int[] allNurses = IntStream.range(0, numNurses).toArray();
final int[] allDays = IntStream.range(0, numDays).toArray();
final int[] allShifts = IntStream.range(0, numShifts).toArray();
```

### C#

```c#
const int numNurses = 4;
const int numDays = 3;
const int numShifts = 3;

int[] allNurses = Enumerable.Range(0, numNurses).ToArray();
int[] allDays = Enumerable.Range(0, numDays).ToArray();
int[] allShifts = Enumerable.Range(0, numShifts).ToArray();
```

### Create the model

The following code creates the model.

### Python

```python
model = cp_model.CpModel()
```

### C++

```c++
CpModelBuilder cp_model;
```

### Java

```java
CpModel model = new CpModel();
```

### C#

```c#
CpModel model = new CpModel();
model.Model.Variables.Capacity = numNurses * numDays * numShifts;
```

### Create the variables

The following code creates an array of variables.

### Python

```python
shifts = {}
for n in all_nurses:
    for d in all_days:
        for s in all_shifts:
            shifts[(n, d, s)] = model.new_bool_var(f"shift_n{n}_d{d}_s{s}")
```

### C++

```c++
std::map<std::tuple<int, int, int>, BoolVar> shifts;
for (int n : all_nurses) {
  for (int d : all_days) {
    for (int s : all_shifts) {
      auto key = std::make_tuple(n, d, s);
      shifts[key] = cp_model.NewBoolVar().WithName(
          absl::StrFormat("shift_n%dd%ds%d", n, d, s));
    }
  }
}
```

### Java

```java
Literal[][][] shifts = new Literal[numNurses][numDays][numShifts];
for (int n : allNurses) {
  for (int d : allDays) {
    for (int s : allShifts) {
      shifts[n][d][s] = model.newBoolVar("shifts_n" + n + "d" + d + "s" + s);
    }
  }
}
```

### C#

```c#
Dictionary<(int, int, int), BoolVar> shifts =
    new Dictionary<(int, int, int), BoolVar>(numNurses * numDays * numShifts);
foreach (int n in allNurses)
{
    foreach (int d in allDays)
    {
        foreach (int s in allShifts)
        {
            shifts.Add((n, d, s), model.NewBoolVar($"shifts_n{n}d{d}s{s}"));
        }
    }
}
```

The array defines assignments for shifts to nurses as follows:
`shifts[(n, d, s)]` equals 1 if shift s is assigned to nurse n on day d, and 0
otherwise.

### Assign nurses to shifts

Next, we show how to assign nurses to shifts subject to the following constraints:

- Each shift is assigned to a single nurse per day.
- Each nurse works at most one shift per day.

Here's the code that creates the first condition.

### Python

```python
for d in all_days:
    for s in all_shifts:
        model.add_exactly_one(shifts[(n, d, s)] for n in all_nurses)
```

### C++

```c++
for (int d : all_days) {
  for (int s : all_shifts) {
    std::vector<BoolVar> nurses;
    for (int n : all_nurses) {
      auto key = std::make_tuple(n, d, s);
      nurses.push_back(shifts[key]);
    }
    cp_model.AddExactlyOne(nurses);
  }
}
```

### Java

```java
for (int d : allDays) {
  for (int s : allShifts) {
    List<Literal> nurses = new ArrayList<>();
    for (int n : allNurses) {
      nurses.add(shifts[n][d][s]);
    }
    model.addExactlyOne(nurses);
  }
}
```

### C#

```c#
List<ILiteral> literals = new List<ILiteral>();
foreach (int d in allDays)
{
    foreach (int s in allShifts)
    {
        foreach (int n in allNurses)
        {
            literals.Add(shifts[(n, d, s)]);
        }
        model.AddExactlyOne(literals);
        literals.Clear();
    }
}
```

The last line says that for each shift, the sum of the nurses assigned to that
shift is 1.

Next, here's the code that requires that each nurse works at most one shift per
day.

### Python

```python
for n in all_nurses:
    for d in all_days:
        model.add_at_most_one(shifts[(n, d, s)] for s in all_shifts)
```

### C++

```c++
for (int n : all_nurses) {
  for (int d : all_days) {
    std::vector<BoolVar> work;
    for (int s : all_shifts) {
      auto key = std::make_tuple(n, d, s);
      work.push_back(shifts[key]);
    }
    cp_model.AddAtMostOne(work);
  }
}
```

### Java

```java
for (int n : allNurses) {
  for (int d : allDays) {
    List<Literal> work = new ArrayList<>();
    for (int s : allShifts) {
      work.add(shifts[n][d][s]);
    }
    model.addAtMostOne(work);
  }
}
```

### C#

```c#
foreach (int n in allNurses)
{
    foreach (int d in allDays)
    {
        foreach (int s in allShifts)
        {
            literals.Add(shifts[(n, d, s)]);
        }
        model.AddAtMostOne(literals);
        literals.Clear();
    }
}
```

For each nurse, the sum of shifts assigned to that nurse is at most 1 ("at most"
because a nurse might have the day off).

### Assign shifts evenly

Next, we show how to assign shifts to nurses as evenly as possible.
Since there are nine shifts over the three-day period, we can assign two shifts
to each of the four nurses.
After that there will be one shift left over, which can be assigned to any nurse.

The following code ensures that each nurse works at least two shifts in the
three-day period.

### Python

```python
# Try to distribute the shifts evenly, so that each nurse works
# min_shifts_per_nurse shifts. If this is not possible, because the total
# number of shifts is not divisible by the number of nurses, some nurses will
# be assigned one more shift.
min_shifts_per_nurse = (num_shifts * num_days) // num_nurses
if num_shifts * num_days % num_nurses == 0:
    max_shifts_per_nurse = min_shifts_per_nurse
else:
    max_shifts_per_nurse = min_shifts_per_nurse + 1
for n in all_nurses:
    shifts_worked = []
    for d in all_days:
        for s in all_shifts:
            shifts_worked.append(shifts[(n, d, s)])
    model.add(min_shifts_per_nurse <= sum(shifts_worked))
    model.add(sum(shifts_worked) <= max_shifts_per_nurse)
```

### C++

```c++
// Try to distribute the shifts evenly, so that each nurse works
// min_shifts_per_nurse shifts. If this is not possible, because the total
// number of shifts is not divisible by the number of nurses, some nurses will
// be assigned one more shift.
int min_shifts_per_nurse = (num_shifts * num_days) / num_nurses;
int max_shifts_per_nurse;
if ((num_shifts * num_days) % num_nurses == 0) {
  max_shifts_per_nurse = min_shifts_per_nurse;
} else {
  max_shifts_per_nurse = min_shifts_per_nurse + 1;
}
for (int n : all_nurses) {
  std::vector<BoolVar> shifts_worked;
  for (int d : all_days) {
    for (int s : all_shifts) {
      auto key = std::make_tuple(n, d, s);
      shifts_worked.push_back(shifts[key]);
    }
  }
  cp_model.AddLessOrEqual(min_shifts_per_nurse,
                          LinearExpr::Sum(shifts_worked));
  cp_model.AddLessOrEqual(LinearExpr::Sum(shifts_worked),
                          max_shifts_per_nurse);
}
```

### Java

```java
// Try to distribute the shifts evenly, so that each nurse works
// minShiftsPerNurse shifts. If this is not possible, because the total
// number of shifts is not divisible by the number of nurses, some nurses will
// be assigned one more shift.
int minShiftsPerNurse = (numShifts * numDays) / numNurses;
int maxShiftsPerNurse;
if ((numShifts * numDays) % numNurses == 0) {
  maxShiftsPerNurse = minShiftsPerNurse;
} else {
  maxShiftsPerNurse = minShiftsPerNurse + 1;
}
for (int n : allNurses) {
  LinearExprBuilder shiftsWorked = LinearExpr.newBuilder();
  for (int d : allDays) {
    for (int s : allShifts) {
      shiftsWorked.add(shifts[n][d][s]);
    }
  }
  model.addLinearConstraint(shiftsWorked, minShiftsPerNurse, maxShiftsPerNurse);
}
```

### C#

```c#
// Try to distribute the shifts evenly, so that each nurse works
// minShiftsPerNurse shifts. If this is not possible, because the total
// number of shifts is not divisible by the number of nurses, some nurses will
// be assigned one more shift.
int minShiftsPerNurse = (numShifts * numDays) / numNurses;
int maxShiftsPerNurse;
if ((numShifts * numDays) % numNurses == 0)
{
    maxShiftsPerNurse = minShiftsPerNurse;
}
else
{
    maxShiftsPerNurse = minShiftsPerNurse + 1;
}

List<IntVar> shiftsWorked = new List<IntVar>();
foreach (int n in allNurses)
{
    foreach (int d in allDays)
    {
        foreach (int s in allShifts)
        {
            shiftsWorked.Add(shifts[(n, d, s)]);
        }
    }
    model.AddLinearConstraint(LinearExpr.Sum(shiftsWorked), minShiftsPerNurse, maxShiftsPerNurse);
    shiftsWorked.Clear();
}
```

Since there are `num_shifts * num_days` total shifts in the schedule period, you
can assign at least `(num_shifts * num_days) // num_nurses`

shifts to each nurse, but some shifts may be left over. (Here `//` is the Python
integer division operator, which returns the floor of the usual quotient.)

For the given values of `num_nurses = 4`, `num_shifts = 3`, and `num_days = 3`,
the expression `min_shifts_per_nurse` has the value `(3 * 3 // 4) = 2`, so you
can assign at least two shifts to each nurse. This is specified by the
constraint (here in Python)

```python
model.add(min_shifts_per_nurse <= sum(shifts_worked))
```

<br />

Since there are nine total shifts over the three-day period, there is one
remaining shift after assigning two shifts to each nurse. The extra shift can be
assigned to any nurse.

The final line (here in Python)

```python
model.add(sum(shifts_worked) <= max_shifts_per_nurse)
```

ensures that no nurse is assigned more than one extra shift.

The constraint isn't necessary in this case, because there's only one extra
shift. But for different parameter values, there could be several extra shifts,
in which case the constraint is necessary.

### Update solver parameters

In a non-optimization model, you can enable the search for all solutions.

### Python

```python
solver = cp_model.CpSolver()
solver.parameters.linearization_level = 0
# Enumerate all solutions.
solver.parameters.enumerate_all_solutions = True
```

### C++

```c++
Model model;
SatParameters parameters;
parameters.set_linearization_level(0);
// Enumerate all solutions.
parameters.set_enumerate_all_solutions(true);
model.Add(NewSatParameters(parameters));
```

### Java

```java
CpSolver solver = new CpSolver();
solver.getParameters().setLinearizationLevel(0);
// Tell the solver to enumerate all solutions.
solver.getParameters().setEnumerateAllSolutions(true);
```

### C#

```c#
CpSolver solver = new CpSolver();
// Tell the solver to enumerate all solutions.
solver.StringParameters += "linearization_level:0 " + "enumerate_all_solutions:true ";
```

### Register a Solutions Callback

You need to register a callback on the solver that will be called at each
solution.

### Python

```python
class NursesPartialSolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, shifts, num_nurses, num_days, num_shifts, limit):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self._shifts = shifts
        self._num_nurses = num_nurses
        self._num_days = num_days
        self._num_shifts = num_shifts
        self._solution_count = 0
        self._solution_limit = limit

    def on_solution_callback(self):
        self._solution_count += 1
        print(f"Solution {self._solution_count}")
        for d in range(self._num_days):
            print(f"Day {d}")
            for n in range(self._num_nurses):
                is_working = False
                for s in range(self._num_shifts):
                    if self.value(self._shifts[(n, d, s)]):
                        is_working = True
                        print(f"  Nurse {n} works shift {s}")
                if not is_working:
                    print(f"  Nurse {n} does not work")
        if self._solution_count >= self._solution_limit:
            print(f"Stop search after {self._solution_limit} solutions")
            self.stop_search()

    def solutionCount(self):
        return self._solution_count

# Display the first five solutions.
solution_limit = 5
solution_printer = NursesPartialSolutionPrinter(
    shifts, num_nurses, num_days, num_shifts, solution_limit
)
```

### C++

```c++
const int kSolutionLimit = 5;
int num_solutions = 0;
model.Add(NewFeasibleSolutionObserver([&](const CpSolverResponse& r) {
  LOG(INFO) << "Solution " << num_solutions;
  for (int d : all_days) {
    LOG(INFO) << "Day " << std::to_string(d);
    for (int n : all_nurses) {
      bool is_working = false;
      for (int s : all_shifts) {
        auto key = std::make_tuple(n, d, s);
        if (SolutionIntegerValue(r, shifts[key])) {
          is_working = true;
          LOG(INFO) << "  Nurse " << std::to_string(n) << " works shift "
                    << std::to_string(s);
        }
      }
      if (!is_working) {
        LOG(INFO) << "  Nurse " << std::to_string(n) << " does not work";
      }
    }
  }
  num_solutions++;
  if (num_solutions >= kSolutionLimit) {
    StopSearch(&model);
    LOG(INFO) << "Stop search after " << kSolutionLimit << " solutions.";
  }
}));
```

### Java

```java
final int solutionLimit = 5;
class VarArraySolutionPrinterWithLimit extends CpSolverSolutionCallback {
  public VarArraySolutionPrinterWithLimit(
      int[] allNurses, int[] allDays, int[] allShifts, Literal[][][] shifts, int limit) {
    solutionCount = 0;
    this.allNurses = allNurses;
    this.allDays = allDays;
    this.allShifts = allShifts;
    this.shifts = shifts;
    solutionLimit = limit;
  }

  @Override
  public void onSolutionCallback() {
    System.out.printf("Solution #%d:%n", solutionCount);
    for (int d : allDays) {
      System.out.printf("Day %d%n", d);
      for (int n : allNurses) {
        boolean isWorking = false;
        for (int s : allShifts) {
          if (booleanValue(shifts[n][d][s])) {
            isWorking = true;
            System.out.printf("  Nurse %d work shift %d%n", n, s);
          }
        }
        if (!isWorking) {
          System.out.printf("  Nurse %d does not work%n", n);
        }
      }
    }
    solutionCount++;
    if (solutionCount >= solutionLimit) {
      System.out.printf("Stop search after %d solutions%n", solutionLimit);
      stopSearch();
    }
  }

  public int getSolutionCount() {
    return solutionCount;
  }

  private int solutionCount;
  private final int[] allNurses;
  private final int[] allDays;
  private final int[] allShifts;
  private final Literal[][][] shifts;
  private final int solutionLimit;
}

VarArraySolutionPrinterWithLimit cb =
    new VarArraySolutionPrinterWithLimit(allNurses, allDays, allShifts, shifts, solutionLimit);
```

### C#

First define the `SolutionPrinter` class.

```c#
public class SolutionPrinter : CpSolverSolutionCallback
{
    public SolutionPrinter(int[] allNurses, int[] allDays, int[] allShifts,
                           Dictionary<(int, int, int), BoolVar> shifts, int limit)
    {
        solutionCount_ = 0;
        allNurses_ = allNurses;
        allDays_ = allDays;
        allShifts_ = allShifts;
        shifts_ = shifts;
        solutionLimit_ = limit;
    }

    public override void OnSolutionCallback()
    {
        Console.WriteLine($"Solution #{solutionCount_}:");
        foreach (int d in allDays_)
        {
            Console.WriteLine($"Day {d}");
            foreach (int n in allNurses_)
            {
                bool isWorking = false;
                foreach (int s in allShifts_)
                {
                    if (Value(shifts_[(n, d, s)]) == 1L)
                    {
                        isWorking = true;
                        Console.WriteLine($"  Nurse {n} work shift {s}");
                    }
                }
                if (!isWorking)
                {
                    Console.WriteLine($"  Nurse {d} does not work");
                }
            }
        }
        solutionCount_++;
        if (solutionCount_ >= solutionLimit_)
        {
            Console.WriteLine($"Stop search after {solutionLimit_} solutions");
            StopSearch();
        }
    }

    public int SolutionCount()
    {
        return solutionCount_;
    }

    private int solutionCount_;
    private int[] allNurses_;
    private int[] allDays_;
    private int[] allShifts_;
    private Dictionary<(int, int, int), BoolVar> shifts_;
    private int solutionLimit_;
}
```
Then instantiate it using:

```c#
const int solutionLimit = 5;
SolutionPrinter cb = new SolutionPrinter(allNurses, allDays, allShifts, shifts, solutionLimit);
```

### Invoke the solver

The following code calls the solver and displays the first five solutions.

### Python

```python
solver.solve(model, solution_printer)
```

### C++

```c++
const CpSolverResponse response = SolveCpModel(cp_model.Build(), &model);
```

### Java

```java
CpSolverStatus status = solver.solve(model, cb);
System.out.println("Status: " + status);
System.out.println(cb.getSolutionCount() + " solutions found.");
```

### C#

```c#
CpSolverStatus status = solver.Solve(model, cb);
Console.WriteLine($"Solve status: {status}");
```

### Solutions

Here are the first five solutions.

    Solution 0
    Day 0
    Nurse 0 does not work
    Nurse 1 works shift 0
    Nurse 2 works shift 1
    Nurse 3 works shift 2
    Day 1
    Nurse 0 works shift 2
    Nurse 1 does not work
    Nurse 2 works shift 1
    Nurse 3 works shift 0
    Day 2
    Nurse 0 works shift 2
    Nurse 1 works shift 1
    Nurse 2 works shift 0
    Nurse 3 does not work

    Solution 1
    Day 0
    Nurse 0 works shift 0
    Nurse 1 does not work
    Nurse 2 works shift 1
    Nurse 3 works shift 2
    Day 1
    Nurse 0 does not work
    Nurse 1 works shift 2
    Nurse 2 works shift 1
    Nurse 3 works shift 0
    Day 2
    Nurse 0 works shift 2
    Nurse 1 works shift 1
    Nurse 2 works shift 0
    Nurse 3 does not work

    Solution 2
    Day 0 Nurse 0 works shift 0
    Nurse 1 does not work
    Nurse 2 works shift 1
    Nurse 3 works shift 2
    Day 1
    Nurse 0 works shift 1
    Nurse 1 works shift 2
    Nurse 2 does not work
    Nurse 3 works shift 0
    Day 2
    Nurse 0 works shift 2
    Nurse 1 works shift 1
    Nurse 2 works shift 0
    Nurse 3 does not work

    Solution 3
    Day 0 Nurse 0 does not work
    Nurse 1 works shift 0
    Nurse 2 works shift 1
    Nurse 3 works shift 2
    Day 1
    Nurse 0 works shift 1
    Nurse 1 works shift 2
    Nurse 2 does not work
    Nurse 3 works shift 0
    Day 2
    Nurse 0 works shift 2
    Nurse 1 works shift 1
    Nurse 2 works shift 0
    Nurse 3 does not work

    Solution 4
    Day 0
    Nurse 0 does not work
    Nurse 1 works shift 0
    Nurse 2 works shift 1
    Nurse 3 works shift 2
    Day 1
    Nurse 0 works shift 2
    Nurse 1 works shift 1
    Nurse 2 does not work
    Nurse 3 works shift 0
    Day 2
    Nurse 0 works shift 2
    Nurse 1 works shift 1
    Nurse 2 works shift 0
    Nurse 3 does not work

    Statistics
      - conflicts      : 5
      - branches       : 142
      - wall time      : 0.002484 s
      - solutions found: 5

The total number of solutions is 5184.
The following counting argument explains why.

First, there are 4 choices for the one nurse who works an extra shift.
Having chosen that nurse, there are 3 shifts the nurse can be assigned to on
each of the 3 days, so the number of possible ways to assign the nurse with the
extra shift is 4 · 3^3^ = 108.
After assigning this nurse, there are two remaining unassigned shifts on each day.

Of the remaining three nurses, one works days 0 and 1, one works days 0 and 2,
and one works days 1 and 2.
There are 3! = 6 ways to assign the nurses to these days, as shown in the
diagram below. (The three nurses are labeled A, B, and C, and we have not yet
assigned them to shifts.)

    Day 0    Day 1    Day 2
     A B      A C      B C
     A B      B C      A C
     A C      A B      B C
     A C      B C      A B
     B C      A B      A C
     B C      A C      A B

For each row in the above diagram, there are 2^3^ = 8 possible ways to
assign the remaining shifts to the nurses (two choices on each day).
So the total number of possible assignments is 108·6·8 = 5184.

### Entire program

Here is the entire program for the nurse scheduling problem.

### Python

```python
"""Example of a simple nurse scheduling problem."""
from ortools.sat.python import cp_model



def main() -> None:
    # Data.
    num_nurses = 4
    num_shifts = 3
    num_days = 3
    all_nurses = range(num_nurses)
    all_shifts = range(num_shifts)
    all_days = range(num_days)

    # Creates the model.
    model = cp_model.CpModel()

    # Creates shift variables.
    # shifts[(n, d, s)]: nurse 'n' works shift 's' on day 'd'.
    shifts = {}
    for n in all_nurses:
        for d in all_days:
            for s in all_shifts:
                shifts[(n, d, s)] = model.new_bool_var(f"shift_n{n}_d{d}_s{s}")

    # Each shift is assigned to exactly one nurse in the schedule period.
    for d in all_days:
        for s in all_shifts:
            model.add_exactly_one(shifts[(n, d, s)] for n in all_nurses)

    # Each nurse works at most one shift per day.
    for n in all_nurses:
        for d in all_days:
            model.add_at_most_one(shifts[(n, d, s)] for s in all_shifts)

    # Try to distribute the shifts evenly, so that each nurse works
    # min_shifts_per_nurse shifts. If this is not possible, because the total
    # number of shifts is not divisible by the number of nurses, some nurses will
    # be assigned one more shift.
    min_shifts_per_nurse = (num_shifts * num_days) // num_nurses
    if num_shifts * num_days % num_nurses == 0:
        max_shifts_per_nurse = min_shifts_per_nurse
    else:
        max_shifts_per_nurse = min_shifts_per_nurse + 1
    for n in all_nurses:
        shifts_worked = []
        for d in all_days:
            for s in all_shifts:
                shifts_worked.append(shifts[(n, d, s)])
        model.add(min_shifts_per_nurse <= sum(shifts_worked))
        model.add(sum(shifts_worked) <= max_shifts_per_nurse)

    # Creates the solver and solve.
    solver = cp_model.CpSolver()
    solver.parameters.linearization_level = 0
    # Enumerate all solutions.
    solver.parameters.enumerate_all_solutions = True

    class NursesPartialSolutionPrinter(cp_model.CpSolverSolutionCallback):
        """Print intermediate solutions."""

        def __init__(self, shifts, num_nurses, num_days, num_shifts, limit):
            cp_model.CpSolverSolutionCallback.__init__(self)
            self._shifts = shifts
            self._num_nurses = num_nurses
            self._num_days = num_days
            self._num_shifts = num_shifts
            self._solution_count = 0
            self._solution_limit = limit

        def on_solution_callback(self):
            self._solution_count += 1
            print(f"Solution {self._solution_count}")
            for d in range(self._num_days):
                print(f"Day {d}")
                for n in range(self._num_nurses):
                    is_working = False
                    for s in range(self._num_shifts):
                        if self.value(self._shifts[(n, d, s)]):
                            is_working = True
                            print(f"  Nurse {n} works shift {s}")
                    if not is_working:
                        print(f"  Nurse {n} does not work")
            if self._solution_count >= self._solution_limit:
                print(f"Stop search after {self._solution_limit} solutions")
                self.stop_search()

        def solutionCount(self):
            return self._solution_count

    # Display the first five solutions.
    solution_limit = 5
    solution_printer = NursesPartialSolutionPrinter(
        shifts, num_nurses, num_days, num_shifts, solution_limit
    )

    solver.solve(model, solution_printer)

    # Statistics.
    print("\nStatistics")
    print(f"  - conflicts      : {solver.num_conflicts}")
    print(f"  - branches       : {solver.num_branches}")
    print(f"  - wall time      : {solver.wall_time} s")
    print(f"  - solutions found: {solution_printer.solutionCount()}")


if __name__ == "__main__":
    main()
```

### C++

```c++
// Example of a simple nurse scheduling problem.
#include <stdlib.h>

#include <atomic>
#include <map>
#include <numeric>
#include <string>
#include <tuple>
#include <vector>

#include "absl/base/log_severity.h"
#include "absl/log/globals.h"
#include "absl/strings/str_format.h"
#include "ortools/base/init_google.h"
#include "ortools/base/logging.h"
#include "ortools/sat/cp_model.h"
#include "ortools/sat/cp_model.pb.h"
#include "ortools/sat/cp_model_solver.h"
#include "ortools/sat/model.h"
#include "ortools/sat/sat_parameters.pb.h"
#include "ortools/util/time_limit.h"

namespace operations_research {
namespace sat {

void NurseSat() {
  const int num_nurses = 4;
  const int num_shifts = 3;
  const int num_days = 3;

  std::vector<int> all_nurses(num_nurses);
  std::iota(all_nurses.begin(), all_nurses.end(), 0);

  std::vector<int> all_shifts(num_shifts);
  std::iota(all_shifts.begin(), all_shifts.end(), 0);

  std::vector<int> all_days(num_days);
  std::iota(all_days.begin(), all_days.end(), 0);

  // Creates the model.
  CpModelBuilder cp_model;

  // Creates shift variables.
  // shifts[(n, d, s)]: nurse 'n' works shift 's' on day 'd'.
  std::map<std::tuple<int, int, int>, BoolVar> shifts;
  for (int n : all_nurses) {
    for (int d : all_days) {
      for (int s : all_shifts) {
        auto key = std::make_tuple(n, d, s);
        shifts[key] = cp_model.NewBoolVar().WithName(
            absl::StrFormat("shift_n%dd%ds%d", n, d, s));
      }
    }
  }

  // Each shift is assigned to exactly one nurse in the schedule period.
  for (int d : all_days) {
    for (int s : all_shifts) {
      std::vector<BoolVar> nurses;
      for (int n : all_nurses) {
        auto key = std::make_tuple(n, d, s);
        nurses.push_back(shifts[key]);
      }
      cp_model.AddExactlyOne(nurses);
    }
  }

  // Each nurse works at most one shift per day.
  for (int n : all_nurses) {
    for (int d : all_days) {
      std::vector<BoolVar> work;
      for (int s : all_shifts) {
        auto key = std::make_tuple(n, d, s);
        work.push_back(shifts[key]);
      }
      cp_model.AddAtMostOne(work);
    }
  }

  // Try to distribute the shifts evenly, so that each nurse works
  // min_shifts_per_nurse shifts. If this is not possible, because the total
  // number of shifts is not divisible by the number of nurses, some nurses will
  // be assigned one more shift.
  int min_shifts_per_nurse = (num_shifts * num_days) / num_nurses;
  int max_shifts_per_nurse;
  if ((num_shifts * num_days) % num_nurses == 0) {
    max_shifts_per_nurse = min_shifts_per_nurse;
  } else {
    max_shifts_per_nurse = min_shifts_per_nurse + 1;
  }
  for (int n : all_nurses) {
    std::vector<BoolVar> shifts_worked;
    for (int d : all_days) {
      for (int s : all_shifts) {
        auto key = std::make_tuple(n, d, s);
        shifts_worked.push_back(shifts[key]);
      }
    }
    cp_model.AddLessOrEqual(min_shifts_per_nurse,
                            LinearExpr::Sum(shifts_worked));
    cp_model.AddLessOrEqual(LinearExpr::Sum(shifts_worked),
                            max_shifts_per_nurse);
  }

  Model model;
  SatParameters parameters;
  parameters.set_linearization_level(0);
  // Enumerate all solutions.
  parameters.set_enumerate_all_solutions(true);
  model.Add(NewSatParameters(parameters));

  // Display the first five solutions.
  const int kSolutionLimit = 5;
  int num_solutions = 0;
  model.Add(NewFeasibleSolutionObserver([&](const CpSolverResponse& r) {
    LOG(INFO) << "Solution " << num_solutions;
    for (int d : all_days) {
      LOG(INFO) << "Day " << std::to_string(d);
      for (int n : all_nurses) {
        bool is_working = false;
        for (int s : all_shifts) {
          auto key = std::make_tuple(n, d, s);
          if (SolutionIntegerValue(r, shifts[key])) {
            is_working = true;
            LOG(INFO) << "  Nurse " << std::to_string(n) << " works shift "
                      << std::to_string(s);
          }
        }
        if (!is_working) {
          LOG(INFO) << "  Nurse " << std::to_string(n) << " does not work";
        }
      }
    }
    num_solutions++;
    if (num_solutions >= kSolutionLimit) {
      StopSearch(&model);
      LOG(INFO) << "Stop search after " << kSolutionLimit << " solutions.";
    }
  }));

  const CpSolverResponse response = SolveCpModel(cp_model.Build(), &model);

  // Statistics.
  LOG(INFO) << "Statistics";
  LOG(INFO) << CpSolverResponseStats(response);
  LOG(INFO) << "solutions found : " << std::to_string(num_solutions);
}

}  // namespace sat
}  // namespace operations_research

int main(int argc, char* argv[]) {
  InitGoogle(argv[0], &argc, &argv, true);
  absl::SetStderrThreshold(absl::LogSeverityAtLeast::kInfo);
  operations_research::sat::NurseSat();
  return EXIT_SUCCESS;
}
```

### Java

```java
package com.google.ortools.sat.samples;
import com.google.ortools.Loader;
import com.google.ortools.sat.CpModel;
import com.google.ortools.sat.CpSolver;
import com.google.ortools.sat.CpSolverSolutionCallback;
import com.google.ortools.sat.CpSolverStatus;
import com.google.ortools.sat.LinearExpr;
import com.google.ortools.sat.LinearExprBuilder;
import com.google.ortools.sat.Literal;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.IntStream;

/** Nurses problem. */
public class NursesSat {
  public static void main(String[] args) {
    Loader.loadNativeLibraries();
    final int numNurses = 4;
    final int numDays = 3;
    final int numShifts = 3;

    final int[] allNurses = IntStream.range(0, numNurses).toArray();
    final int[] allDays = IntStream.range(0, numDays).toArray();
    final int[] allShifts = IntStream.range(0, numShifts).toArray();

    // Creates the model.
    CpModel model = new CpModel();

    // Creates shift variables.
    // shifts[(n, d, s)]: nurse 'n' works shift 's' on day 'd'.
    Literal[][][] shifts = new Literal[numNurses][numDays][numShifts];
    for (int n : allNurses) {
      for (int d : allDays) {
        for (int s : allShifts) {
          shifts[n][d][s] = model.newBoolVar("shifts_n" + n + "d" + d + "s" + s);
        }
      }
    }

    // Each shift is assigned to exactly one nurse in the schedule period.
    for (int d : allDays) {
      for (int s : allShifts) {
        List<Literal> nurses = new ArrayList<>();
        for (int n : allNurses) {
          nurses.add(shifts[n][d][s]);
        }
        model.addExactlyOne(nurses);
      }
    }

    // Each nurse works at most one shift per day.
    for (int n : allNurses) {
      for (int d : allDays) {
        List<Literal> work = new ArrayList<>();
        for (int s : allShifts) {
          work.add(shifts[n][d][s]);
        }
        model.addAtMostOne(work);
      }
    }

    // Try to distribute the shifts evenly, so that each nurse works
    // minShiftsPerNurse shifts. If this is not possible, because the total
    // number of shifts is not divisible by the number of nurses, some nurses will
    // be assigned one more shift.
    int minShiftsPerNurse = (numShifts * numDays) / numNurses;
    int maxShiftsPerNurse;
    if ((numShifts * numDays) % numNurses == 0) {
      maxShiftsPerNurse = minShiftsPerNurse;
    } else {
      maxShiftsPerNurse = minShiftsPerNurse + 1;
    }
    for (int n : allNurses) {
      LinearExprBuilder shiftsWorked = LinearExpr.newBuilder();
      for (int d : allDays) {
        for (int s : allShifts) {
          shiftsWorked.add(shifts[n][d][s]);
        }
      }
      model.addLinearConstraint(shiftsWorked, minShiftsPerNurse, maxShiftsPerNurse);
    }

    CpSolver solver = new CpSolver();
    solver.getParameters().setLinearizationLevel(0);
    // Tell the solver to enumerate all solutions.
    solver.getParameters().setEnumerateAllSolutions(true);

    // Display the first five solutions.
    final int solutionLimit = 5;
    class VarArraySolutionPrinterWithLimit extends CpSolverSolutionCallback {
      public VarArraySolutionPrinterWithLimit(
          int[] allNurses, int[] allDays, int[] allShifts, Literal[][][] shifts, int limit) {
        solutionCount = 0;
        this.allNurses = allNurses;
        this.allDays = allDays;
        this.allShifts = allShifts;
        this.shifts = shifts;
        solutionLimit = limit;
      }

      @Override
      public void onSolutionCallback() {
        System.out.printf("Solution #%d:%n", solutionCount);
        for (int d : allDays) {
          System.out.printf("Day %d%n", d);
          for (int n : allNurses) {
            boolean isWorking = false;
            for (int s : allShifts) {
              if (booleanValue(shifts[n][d][s])) {
                isWorking = true;
                System.out.printf("  Nurse %d work shift %d%n", n, s);
              }
            }
            if (!isWorking) {
              System.out.printf("  Nurse %d does not work%n", n);
            }
          }
        }
        solutionCount++;
        if (solutionCount >= solutionLimit) {
          System.out.printf("Stop search after %d solutions%n", solutionLimit);
          stopSearch();
        }
      }

      public int getSolutionCount() {
        return solutionCount;
      }

      private int solutionCount;
      private final int[] allNurses;
      private final int[] allDays;
      private final int[] allShifts;
      private final Literal[][][] shifts;
      private final int solutionLimit;
    }

    VarArraySolutionPrinterWithLimit cb =
        new VarArraySolutionPrinterWithLimit(allNurses, allDays, allShifts, shifts, solutionLimit);

    // Creates a solver and solves the model.
    CpSolverStatus status = solver.solve(model, cb);
    System.out.println("Status: " + status);
    System.out.println(cb.getSolutionCount() + " solutions found.");

    // Statistics.
    System.out.println("Statistics");
    System.out.printf("  conflicts: %d%n", solver.numConflicts());
    System.out.printf("  branches : %d%n", solver.numBranches());
    System.out.printf("  wall time: %f s%n", solver.wallTime());
  }

  private NursesSat() {}
}
```

### C#

```c#
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using Google.OrTools.Sat;

public class NursesSat
{
    public class SolutionPrinter : CpSolverSolutionCallback
    {
        public SolutionPrinter(int[] allNurses, int[] allDays, int[] allShifts,
                               Dictionary<(int, int, int), BoolVar> shifts, int limit)
        {
            solutionCount_ = 0;
            allNurses_ = allNurses;
            allDays_ = allDays;
            allShifts_ = allShifts;
            shifts_ = shifts;
            solutionLimit_ = limit;
        }

        public override void OnSolutionCallback()
        {
            Console.WriteLine($"Solution #{solutionCount_}:");
            foreach (int d in allDays_)
            {
                Console.WriteLine($"Day {d}");
                foreach (int n in allNurses_)
                {
                    bool isWorking = false;
                    foreach (int s in allShifts_)
                    {
                        if (Value(shifts_[(n, d, s)]) == 1L)
                        {
                            isWorking = true;
                            Console.WriteLine($"  Nurse {n} work shift {s}");
                        }
                    }
                    if (!isWorking)
                    {
                        Console.WriteLine($"  Nurse {d} does not work");
                    }
                }
            }
            solutionCount_++;
            if (solutionCount_ >= solutionLimit_)
            {
                Console.WriteLine($"Stop search after {solutionLimit_} solutions");
                StopSearch();
            }
        }

        public int SolutionCount()
        {
            return solutionCount_;
        }

        private int solutionCount_;
        private int[] allNurses_;
        private int[] allDays_;
        private int[] allShifts_;
        private Dictionary<(int, int, int), BoolVar> shifts_;
        private int solutionLimit_;
    }

    public static void Main(String[] args)
    {
        const int numNurses = 4;
        const int numDays = 3;
        const int numShifts = 3;

        int[] allNurses = Enumerable.Range(0, numNurses).ToArray();
        int[] allDays = Enumerable.Range(0, numDays).ToArray();
        int[] allShifts = Enumerable.Range(0, numShifts).ToArray();

        // Creates the model.
        CpModel model = new CpModel();
        model.Model.Variables.Capacity = numNurses * numDays * numShifts;

        // Creates shift variables.
        // shifts[(n, d, s)]: nurse 'n' works shift 's' on day 'd'.
        Dictionary<(int, int, int), BoolVar> shifts =
            new Dictionary<(int, int, int), BoolVar>(numNurses * numDays * numShifts);
        foreach (int n in allNurses)
        {
            foreach (int d in allDays)
            {
                foreach (int s in allShifts)
                {
                    shifts.Add((n, d, s), model.NewBoolVar($"shifts_n{n}d{d}s{s}"));
                }
            }
        }

        // Each shift is assigned to exactly one nurse in the schedule period.
        List<ILiteral> literals = new List<ILiteral>();
        foreach (int d in allDays)
        {
            foreach (int s in allShifts)
            {
                foreach (int n in allNurses)
                {
                    literals.Add(shifts[(n, d, s)]);
                }
                model.AddExactlyOne(literals);
                literals.Clear();
            }
        }

        // Each nurse works at most one shift per day.
        foreach (int n in allNurses)
        {
            foreach (int d in allDays)
            {
                foreach (int s in allShifts)
                {
                    literals.Add(shifts[(n, d, s)]);
                }
                model.AddAtMostOne(literals);
                literals.Clear();
            }
        }

        // Try to distribute the shifts evenly, so that each nurse works
        // minShiftsPerNurse shifts. If this is not possible, because the total
        // number of shifts is not divisible by the number of nurses, some nurses will
        // be assigned one more shift.
        int minShiftsPerNurse = (numShifts * numDays) / numNurses;
        int maxShiftsPerNurse;
        if ((numShifts * numDays) % numNurses == 0)
        {
            maxShiftsPerNurse = minShiftsPerNurse;
        }
        else
        {
            maxShiftsPerNurse = minShiftsPerNurse + 1;
        }

        List<IntVar> shiftsWorked = new List<IntVar>();
        foreach (int n in allNurses)
        {
            foreach (int d in allDays)
            {
                foreach (int s in allShifts)
                {
                    shiftsWorked.Add(shifts[(n, d, s)]);
                }
            }
            model.AddLinearConstraint(LinearExpr.Sum(shiftsWorked), minShiftsPerNurse, maxShiftsPerNurse);
            shiftsWorked.Clear();
        }

        CpSolver solver = new CpSolver();
        // Tell the solver to enumerate all solutions.
        solver.StringParameters += "linearization_level:0 " + "enumerate_all_solutions:true ";

        // Display the first five solutions.
        const int solutionLimit = 5;
        SolutionPrinter cb = new SolutionPrinter(allNurses, allDays, allShifts, shifts, solutionLimit);

        // Solve
        CpSolverStatus status = solver.Solve(model, cb);
        Console.WriteLine($"Solve status: {status}");

        Console.WriteLine("Statistics");
        Console.WriteLine($"  conflicts: {solver.NumConflicts()}");
        Console.WriteLine($"  branches : {solver.NumBranches()}");
        Console.WriteLine($"  wall time: {solver.WallTime()}s");
    }
}
```

## Scheduling with shift requests

In this section, we take the previous example and add nurse requests for
specific shifts.
We then look for a schedule that maximizes the number of requests that are met.
For most scheduling problems, it's best to optimize an objective function, as it
is usually not practical to print all possible schedules.

This example has the same constraints as the previous example.

### Import the libraries

The following code imports the required library.

### Python

```python
from typing import Union

from ortools.sat.python import cp_model
```

### C++

```c++
#include <stdlib.h>

#include <cstdint>
#include <map>
#include <numeric>
#include <string>
#include <tuple>
#include <vector>

#include "absl/base/log_severity.h"
#include "absl/log/globals.h"
#include "absl/strings/str_format.h"
#include "ortools/base/init_google.h"
#include "ortools/base/logging.h"
#include "ortools/sat/cp_model.h"
#include "ortools/sat/cp_model.pb.h"
#include "ortools/sat/cp_model_solver.h"
```

### Java

```java
import com.google.ortools.Loader;
import com.google.ortools.sat.CpModel;
import com.google.ortools.sat.CpSolver;
import com.google.ortools.sat.CpSolverStatus;
import com.google.ortools.sat.LinearExpr;
import com.google.ortools.sat.LinearExprBuilder;
import com.google.ortools.sat.Literal;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.IntStream;
```

### C#

```c#
using System;
using System.Collections.Generic;
using System.Linq;
using Google.OrTools.Sat;
```

### Data for the example

The data for this example is shown after.

### Python

```python
num_nurses = 5
num_shifts = 3
num_days = 7
all_nurses = range(num_nurses)
all_shifts = range(num_shifts)
all_days = range(num_days)
shift_requests = [
    [[0, 0, 1], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, 1]],
    [[0, 0, 0], [0, 0, 0], [0, 1, 0], [0, 1, 0], [1, 0, 0], [0, 0, 0], [0, 0, 1]],
    [[0, 1, 0], [0, 1, 0], [0, 0, 0], [1, 0, 0], [0, 0, 0], [0, 1, 0], [0, 0, 0]],
    [[0, 0, 1], [0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 0], [1, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 0]],
]
```

### C++

```c++
const int num_nurses = 5;
const int num_days = 7;
const int num_shifts = 3;

std::vector<int> all_nurses(num_nurses);
std::iota(all_nurses.begin(), all_nurses.end(), 0);

std::vector<int> all_days(num_days);
std::iota(all_days.begin(), all_days.end(), 0);

std::vector<int> all_shifts(num_shifts);
std::iota(all_shifts.begin(), all_shifts.end(), 0);

std::vector<std::vector<std::vector<int64_t>>> shift_requests = {
    {
        {0, 0, 1},
        {0, 0, 0},
        {0, 0, 0},
        {0, 0, 0},
        {0, 0, 1},
        {0, 1, 0},
        {0, 0, 1},
    },
    {
        {0, 0, 0},
        {0, 0, 0},
        {0, 1, 0},
        {0, 1, 0},
        {1, 0, 0},
        {0, 0, 0},
        {0, 0, 1},
    },
    {
        {0, 1, 0},
        {0, 1, 0},
        {0, 0, 0},
        {1, 0, 0},
        {0, 0, 0},
        {0, 1, 0},
        {0, 0, 0},
    },
    {
        {0, 0, 1},
        {0, 0, 0},
        {1, 0, 0},
        {0, 1, 0},
        {0, 0, 0},
        {1, 0, 0},
        {0, 0, 0},
    },
    {
        {0, 0, 0},
        {0, 0, 1},
        {0, 1, 0},
        {0, 0, 0},
        {1, 0, 0},
        {0, 1, 0},
        {0, 0, 0},
    },
};
```

### Java

```java
final int numNurses = 5;
final int numDays = 7;
final int numShifts = 3;

final int[] allNurses = IntStream.range(0, numNurses).toArray();
final int[] allDays = IntStream.range(0, numDays).toArray();
final int[] allShifts = IntStream.range(0, numShifts).toArray();

final int[][][] shiftRequests = new int[][][] {
    {
        {0, 0, 1},
        {0, 0, 0},
        {0, 0, 0},
        {0, 0, 0},
        {0, 0, 1},
        {0, 1, 0},
        {0, 0, 1},
    },
    {
        {0, 0, 0},
        {0, 0, 0},
        {0, 1, 0},
        {0, 1, 0},
        {1, 0, 0},
        {0, 0, 0},
        {0, 0, 1},
    },
    {
        {0, 1, 0},
        {0, 1, 0},
        {0, 0, 0},
        {1, 0, 0},
        {0, 0, 0},
        {0, 1, 0},
        {0, 0, 0},
    },
    {
        {0, 0, 1},
        {0, 0, 0},
        {1, 0, 0},
        {0, 1, 0},
        {0, 0, 0},
        {1, 0, 0},
        {0, 0, 0},
    },
    {
        {0, 0, 0},
        {0, 0, 1},
        {0, 1, 0},
        {0, 0, 0},
        {1, 0, 0},
        {0, 1, 0},
        {0, 0, 0},
    },
};
```

### C#

```c#
const int numNurses = 5;
const int numDays = 7;
const int numShifts = 3;

int[] allNurses = Enumerable.Range(0, numNurses).ToArray();
int[] allDays = Enumerable.Range(0, numDays).ToArray();
int[] allShifts = Enumerable.Range(0, numShifts).ToArray();

int[,,] shiftRequests = new int[,,] {
    {
        { 0, 0, 1 },
        { 0, 0, 0 },
        { 0, 0, 0 },
        { 0, 0, 0 },
        { 0, 0, 1 },
        { 0, 1, 0 },
        { 0, 0, 1 },
    },
    {
        { 0, 0, 0 },
        { 0, 0, 0 },
        { 0, 1, 0 },
        { 0, 1, 0 },
        { 1, 0, 0 },
        { 0, 0, 0 },
        { 0, 0, 1 },
    },
    {
        { 0, 1, 0 },
        { 0, 1, 0 },
        { 0, 0, 0 },
        { 1, 0, 0 },
        { 0, 0, 0 },
        { 0, 1, 0 },
        { 0, 0, 0 },
    },
    {
        { 0, 0, 1 },
        { 0, 0, 0 },
        { 1, 0, 0 },
        { 0, 1, 0 },
        { 0, 0, 0 },
        { 1, 0, 0 },
        { 0, 0, 0 },
    },
    {
        { 0, 0, 0 },
        { 0, 0, 1 },
        { 0, 1, 0 },
        { 0, 0, 0 },
        { 1, 0, 0 },
        { 0, 1, 0 },
        { 0, 0, 0 },
    },
};
```

### Create the model

The following code creates the model.

### Python

```python
model = cp_model.CpModel()
```

### C++

```c++
CpModelBuilder cp_model;
```

### Java

```java
CpModel model = new CpModel();
```

### C#

```c#
CpModel model = new CpModel();
```

### Create the variables

The following code an array of variables for the problem.

In addition to the variables from the previous example, the data also contains a
set of triples, corresponding to the three shifts per day. Each element of the
triple is 0 or 1, indicating whether a shift was requested. For example, the
triple \[0, 0, 1\] in the fifth position of row 1 indicates that nurse 1 requests
shift 3 on day 5.

### Python

```python
shifts = {}
for n in all_nurses:
    for d in all_days:
        for s in all_shifts:
            shifts[(n, d, s)] = model.new_bool_var(f"shift_n{n}_d{d}_s{s}")
```

### C++

```c++
std::map<std::tuple<int, int, int>, BoolVar> shifts;
for (int n : all_nurses) {
  for (int d : all_days) {
    for (int s : all_shifts) {
      auto key = std::make_tuple(n, d, s);
      shifts[key] = cp_model.NewBoolVar().WithName(
          absl::StrFormat("shift_n%dd%ds%d", n, d, s));
    }
  }
}
```

### Java

```java
Literal[][][] shifts = new Literal[numNurses][numDays][numShifts];
for (int n : allNurses) {
  for (int d : allDays) {
    for (int s : allShifts) {
      shifts[n][d][s] = model.newBoolVar("shifts_n" + n + "d" + d + "s" + s);
    }
  }
}
```

### C#

```c#
Dictionary<Tuple<int, int, int>, IntVar> shifts = new Dictionary<Tuple<int, int, int>, IntVar>();
foreach (int n in allNurses)
{
    foreach (int d in allDays)
    {
        foreach (int s in allShifts)
        {
            shifts.Add(Tuple.Create(n, d, s), model.NewBoolVar($"shifts_n{n}d{d}s{s}"));
        }
    }
}
```

### Create the constraints

The following code create the constraints for the problem.

### Python

```python
for d in all_days:
    for s in all_shifts:
        model.add_exactly_one(shifts[(n, d, s)] for n in all_nurses)
```

### C++

```c++
for (int d : all_days) {
  for (int s : all_shifts) {
    std::vector<BoolVar> nurses;
    for (int n : all_nurses) {
      auto key = std::make_tuple(n, d, s);
      nurses.push_back(shifts[key]);
    }
    cp_model.AddExactlyOne(nurses);
  }
}
```

### Java

```java
for (int d : allDays) {
  for (int s : allShifts) {
    List<Literal> nurses = new ArrayList<>();
    for (int n : allNurses) {
      nurses.add(shifts[n][d][s]);
    }
    model.addExactlyOne(nurses);
  }
}
```

### C#

```c#
foreach (int d in allDays)
{
    foreach (int s in allShifts)
    {
        IntVar[] x = new IntVar[numNurses];
        foreach (int n in allNurses)
        {
            var key = Tuple.Create(n, d, s);
            x[n] = shifts[key];
        }
        model.Add(LinearExpr.Sum(x) == 1);
    }
}
```

### Python

```python
for n in all_nurses:
    for d in all_days:
        model.add_at_most_one(shifts[(n, d, s)] for s in all_shifts)
```

### C++

```c++
for (int n : all_nurses) {
  for (int d : all_days) {
    std::vector<BoolVar> work;
    for (int s : all_shifts) {
      auto key = std::make_tuple(n, d, s);
      work.push_back(shifts[key]);
    }
    cp_model.AddAtMostOne(work);
  }
}
```

### Java

```java
for (int n : allNurses) {
  for (int d : allDays) {
    List<Literal> work = new ArrayList<>();
    for (int s : allShifts) {
      work.add(shifts[n][d][s]);
    }
    model.addAtMostOne(work);
  }
}
```

### C#

```c#
foreach (int n in allNurses)
{
    foreach (int d in allDays)
    {
        IntVar[] x = new IntVar[numShifts];
        foreach (int s in allShifts)
        {
            var key = Tuple.Create(n, d, s);
            x[s] = shifts[key];
        }
        model.Add(LinearExpr.Sum(x) <= 1);
    }
}
```

### Python

```python
# Try to distribute the shifts evenly, so that each nurse works
# min_shifts_per_nurse shifts. If this is not possible, because the total
# number of shifts is not divisible by the number of nurses, some nurses will
# be assigned one more shift.
min_shifts_per_nurse = (num_shifts * num_days) // num_nurses
if num_shifts * num_days % num_nurses == 0:
    max_shifts_per_nurse = min_shifts_per_nurse
else:
    max_shifts_per_nurse = min_shifts_per_nurse + 1
for n in all_nurses:
    num_shifts_worked: Union[cp_model.LinearExpr, int] = 0
    for d in all_days:
        for s in all_shifts:
            num_shifts_worked += shifts[(n, d, s)]
    model.add(min_shifts_per_nurse <= num_shifts_worked)
    model.add(num_shifts_worked <= max_shifts_per_nurse)
```

### C++

```c++
// Try to distribute the shifts evenly, so that each nurse works
// min_shifts_per_nurse shifts. If this is not possible, because the total
// number of shifts is not divisible by the number of nurses, some nurses will
// be assigned one more shift.
int min_shifts_per_nurse = (num_shifts * num_days) / num_nurses;
int max_shifts_per_nurse;
if ((num_shifts * num_days) % num_nurses == 0) {
  max_shifts_per_nurse = min_shifts_per_nurse;
} else {
  max_shifts_per_nurse = min_shifts_per_nurse + 1;
}
for (int n : all_nurses) {
  LinearExpr num_worked_shifts;
  for (int d : all_days) {
    for (int s : all_shifts) {
      auto key = std::make_tuple(n, d, s);
      num_worked_shifts += shifts[key];
    }
  }
  cp_model.AddLessOrEqual(min_shifts_per_nurse, num_worked_shifts);
  cp_model.AddLessOrEqual(num_worked_shifts, max_shifts_per_nurse);
}
```

### Java

```java
// Try to distribute the shifts evenly, so that each nurse works
// minShiftsPerNurse shifts. If this is not possible, because the total
// number of shifts is not divisible by the number of nurses, some nurses will
// be assigned one more shift.
int minShiftsPerNurse = (numShifts * numDays) / numNurses;
int maxShiftsPerNurse;
if ((numShifts * numDays) % numNurses == 0) {
  maxShiftsPerNurse = minShiftsPerNurse;
} else {
  maxShiftsPerNurse = minShiftsPerNurse + 1;
}
for (int n : allNurses) {
  LinearExprBuilder numShiftsWorked = LinearExpr.newBuilder();
  for (int d : allDays) {
    for (int s : allShifts) {
      numShiftsWorked.add(shifts[n][d][s]);
    }
  }
  model.addLinearConstraint(numShiftsWorked, minShiftsPerNurse, maxShiftsPerNurse);
}
```

### C#

```c#
// Try to distribute the shifts evenly, so that each nurse works
// minShiftsPerNurse shifts. If this is not possible, because the total
// number of shifts is not divisible by the number of nurses, some nurses will
// be assigned one more shift.
int minShiftsPerNurse = (numShifts * numDays) / numNurses;
int maxShiftsPerNurse;
if ((numShifts * numDays) % numNurses == 0)
{
    maxShiftsPerNurse = minShiftsPerNurse;
}
else
{
    maxShiftsPerNurse = minShiftsPerNurse + 1;
}
foreach (int n in allNurses)
{
    IntVar[] numShiftsWorked = new IntVar[numDays * numShifts];
    foreach (int d in allDays)
    {
        foreach (int s in allShifts)
        {
            var key = Tuple.Create(n, d, s);
            numShiftsWorked[d * numShifts + s] = shifts[key];
        }
    }
    model.AddLinearConstraint(LinearExpr.Sum(numShiftsWorked), minShiftsPerNurse, maxShiftsPerNurse);
}
```

### Objective for the example

We want to optimize the following objective function.

### Python

```python
model.maximize(
    sum(
        shift_requests[n][d][s] * shifts[(n, d, s)]
        for n in all_nurses
        for d in all_days
        for s in all_shifts
    )
)
```

### C++

```c++
LinearExpr objective_expr;
for (int n : all_nurses) {
  for (int d : all_days) {
    for (int s : all_shifts) {
      if (shift_requests[n][d][s] == 1) {
        auto key = std::make_tuple(n, d, s);
        objective_expr += shifts[key] * shift_requests[n][d][s];
      }
    }
  }
}
cp_model.Maximize(objective_expr);
```

### Java

```java
LinearExprBuilder obj = LinearExpr.newBuilder();
for (int n : allNurses) {
  for (int d : allDays) {
    for (int s : allShifts) {
      obj.addTerm(shifts[n][d][s], shiftRequests[n][d][s]);
    }
  }
}
model.maximize(obj);
```

### C#

```c#
IntVar[] flatShifts = new IntVar[numNurses * numDays * numShifts];
int[] flatShiftRequests = new int[numNurses * numDays * numShifts];
foreach (int n in allNurses)
{
    foreach (int d in allDays)
    {
        foreach (int s in allShifts)
        {
            var key = Tuple.Create(n, d, s);
            flatShifts[n * numDays * numShifts + d * numShifts + s] = shifts[key];
            flatShiftRequests[n * numDays * numShifts + d * numShifts + s] = shiftRequests[n, d, s];
        }
    }
}
model.Maximize(LinearExpr.WeightedSum(flatShifts, flatShiftRequests));
```

Since `shift_requests[n][d][s] * shifts[(n, d, s)` is 1 if shift `s` is assigned
to nurse `n` on day `d` *and* that nurse requested that shift (and 0 otherwise),
the objective is the number shift of assignments that meet a request.

### Invoke the solver

The following code calls the solver.

### Python

```python
solver = cp_model.CpSolver()
status = solver.solve(model)
```

### C++

```c++
const CpSolverResponse response = Solve(cp_model.Build());
```

### Java

```java
CpSolver solver = new CpSolver();
CpSolverStatus status = solver.solve(model);
```

### C#

```c#
CpSolver solver = new CpSolver();
CpSolverStatus status = solver.Solve(model);
Console.WriteLine($"Solve status: {status}");
```

### Display the results

The following code displays the following output, which contains an optimal
schedule (although perhaps not the only one). The output shows which shift
assignments were requested and the number of request that were met.

### Python

```python
if status == cp_model.OPTIMAL:
    print("Solution:")
    for d in all_days:
        print("Day", d)
        for n in all_nurses:
            for s in all_shifts:
                if solver.value(shifts[(n, d, s)]) == 1:
                    if shift_requests[n][d][s] == 1:
                        print("Nurse", n, "works shift", s, "(requested).")
                    else:
                        print("Nurse", n, "works shift", s, "(not requested).")
        print()
    print(
        f"Number of shift requests met = {solver.objective_value}",
        f"(out of {num_nurses * min_shifts_per_nurse})",
    )
else:
    print("No optimal solution found !")
```

### C++

```c++
if (response.status() == CpSolverStatus::OPTIMAL) {
  LOG(INFO) << "Solution:";
  for (int d : all_days) {
    LOG(INFO) << "Day " << std::to_string(d);
    for (int n : all_nurses) {
      for (int s : all_shifts) {
        auto key = std::make_tuple(n, d, s);
        if (SolutionIntegerValue(response, shifts[key]) == 1) {
          if (shift_requests[n][d][s] == 1) {
            LOG(INFO) << "  Nurse " << std::to_string(n) << " works shift "
                      << std::to_string(s) << " (requested).";
          } else {
            LOG(INFO) << "  Nurse " << std::to_string(n) << " works shift "
                      << std::to_string(s) << " (not requested).";
          }
        }
      }
    }
    LOG(INFO) << "";
  }
  LOG(INFO) << "Number of shift requests met = " << response.objective_value()
            << " (out of " << num_nurses * min_shifts_per_nurse << ")";
} else {
  LOG(INFO) << "No optimal solution found !";
}
```

### Java

```java
if (status == CpSolverStatus.OPTIMAL || status == CpSolverStatus.FEASIBLE) {
  System.out.printf("Solution:%n");
  for (int d : allDays) {
    System.out.printf("Day %d%n", d);
    for (int n : allNurses) {
      for (int s : allShifts) {
        if (solver.booleanValue(shifts[n][d][s])) {
          if (shiftRequests[n][d][s] == 1) {
            System.out.printf("  Nurse %d works shift %d (requested).%n", n, s);
          } else {
            System.out.printf("  Nurse %d works shift %d (not requested).%n", n, s);
          }
        }
      }
    }
  }
  System.out.printf("Number of shift requests met = %f (out of %d)%n", solver.objectiveValue(),
      numNurses * minShiftsPerNurse);
} else {
  System.out.printf("No optimal solution found !");
}
```

### C#

```c#
if (status == CpSolverStatus.Optimal || status == CpSolverStatus.Feasible)
{
    Console.WriteLine("Solution:");
    foreach (int d in allDays)
    {
        Console.WriteLine($"Day {d}");
        foreach (int n in allNurses)
        {
            bool isWorking = false;
            foreach (int s in allShifts)
            {
                var key = Tuple.Create(n, d, s);
                if (solver.Value(shifts[key]) == 1L)
                {
                    if (shiftRequests[n, d, s] == 1)
                    {
                        Console.WriteLine($"  Nurse {n} work shift {s} (requested).");
                    }
                    else
                    {
                        Console.WriteLine($"  Nurse {n} work shift {s} (not requested).");
                    }
                }
            }
        }
    }
    Console.WriteLine(
        $"Number of shift requests met = {solver.ObjectiveValue} (out of {numNurses * minShiftsPerNurse}).");
}
else
{
    Console.WriteLine("No solution found.");
}
```

When you run the program, it displays the following output:

    Day 0
    Nurse 1 works shift 0 (not requested).
    Nurse 2 works shift 1 (requested).
    Nurse 3 works shift 2 (requested).

    Day 1
    Nurse 0 works shift 0 (not requested).
    Nurse 2 works shift 1 (requested).
    Nurse 4 works shift 2 (requested).

    Day 2
    Nurse 1 works shift 2 (not requested).
    Nurse 3 works shift 0 (requested).
    Nurse 4 works shift 1 (requested).

    Day 3
    Nurse 2 works shift 0 (requested).
    Nurse 3 works shift 1 (requested).
    Nurse 4 works shift 2 (not requested).

    Day 4
    Nurse 0 works shift 2 (requested).
    Nurse 1 works shift 0 (requested).
    Nurse 4 works shift 1 (not requested).

    Day 5
    Nurse 0 works shift 2 (not requested).
    Nurse 2 works shift 1 (requested).
    Nurse 3 works shift 0 (requested).

    Day 6
    Nurse 0 works shift 1 (not requested).
    Nurse 1 works shift 2 (requested).
    Nurse 4 works shift 0 (not requested).

    Statistics
      - Number of shift requests met = 13 (out of 20 )
      - wall time       : 0.003571 s

### Entire program

Here is the entire program for scheduling with shift requests.

### Python

```python
"""Nurse scheduling problem with shift requests."""
from typing import Union

from ortools.sat.python import cp_model



def main() -> None:
    # This program tries to find an optimal assignment of nurses to shifts
    # (3 shifts per day, for 7 days), subject to some constraints (see below).
    # Each nurse can request to be assigned to specific shifts.
    # The optimal assignment maximizes the number of fulfilled shift requests.
    num_nurses = 5
    num_shifts = 3
    num_days = 7
    all_nurses = range(num_nurses)
    all_shifts = range(num_shifts)
    all_days = range(num_days)
    shift_requests = [
        [[0, 0, 1], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, 1]],
        [[0, 0, 0], [0, 0, 0], [0, 1, 0], [0, 1, 0], [1, 0, 0], [0, 0, 0], [0, 0, 1]],
        [[0, 1, 0], [0, 1, 0], [0, 0, 0], [1, 0, 0], [0, 0, 0], [0, 1, 0], [0, 0, 0]],
        [[0, 0, 1], [0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 0], [1, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 0]],
    ]

    # Creates the model.
    model = cp_model.CpModel()

    # Creates shift variables.
    # shifts[(n, d, s)]: nurse 'n' works shift 's' on day 'd'.
    shifts = {}
    for n in all_nurses:
        for d in all_days:
            for s in all_shifts:
                shifts[(n, d, s)] = model.new_bool_var(f"shift_n{n}_d{d}_s{s}")

    # Each shift is assigned to exactly one nurse in .
    for d in all_days:
        for s in all_shifts:
            model.add_exactly_one(shifts[(n, d, s)] for n in all_nurses)

    # Each nurse works at most one shift per day.
    for n in all_nurses:
        for d in all_days:
            model.add_at_most_one(shifts[(n, d, s)] for s in all_shifts)

    # Try to distribute the shifts evenly, so that each nurse works
    # min_shifts_per_nurse shifts. If this is not possible, because the total
    # number of shifts is not divisible by the number of nurses, some nurses will
    # be assigned one more shift.
    min_shifts_per_nurse = (num_shifts * num_days) // num_nurses
    if num_shifts * num_days % num_nurses == 0:
        max_shifts_per_nurse = min_shifts_per_nurse
    else:
        max_shifts_per_nurse = min_shifts_per_nurse + 1
    for n in all_nurses:
        num_shifts_worked: Union[cp_model.LinearExpr, int] = 0
        for d in all_days:
            for s in all_shifts:
                num_shifts_worked += shifts[(n, d, s)]
        model.add(min_shifts_per_nurse <= num_shifts_worked)
        model.add(num_shifts_worked <= max_shifts_per_nurse)

    model.maximize(
        sum(
            shift_requests[n][d][s] * shifts[(n, d, s)]
            for n in all_nurses
            for d in all_days
            for s in all_shifts
        )
    )

    # Creates the solver and solve.
    solver = cp_model.CpSolver()
    status = solver.solve(model)

    if status == cp_model.OPTIMAL:
        print("Solution:")
        for d in all_days:
            print("Day", d)
            for n in all_nurses:
                for s in all_shifts:
                    if solver.value(shifts[(n, d, s)]) == 1:
                        if shift_requests[n][d][s] == 1:
                            print("Nurse", n, "works shift", s, "(requested).")
                        else:
                            print("Nurse", n, "works shift", s, "(not requested).")
            print()
        print(
            f"Number of shift requests met = {solver.objective_value}",
            f"(out of {num_nurses * min_shifts_per_nurse})",
        )
    else:
        print("No optimal solution found !")

    # Statistics.
    print("\nStatistics")
    print(f"  - conflicts: {solver.num_conflicts}")
    print(f"  - branches : {solver.num_branches}")
    print(f"  - wall time: {solver.wall_time}s")


if __name__ == "__main__":
    main()
```

### C++

```c++
// Nurse scheduling problem with shift requests.
#include <stdlib.h>

#include <cstdint>
#include <map>
#include <numeric>
#include <string>
#include <tuple>
#include <vector>

#include "absl/base/log_severity.h"
#include "absl/log/globals.h"
#include "absl/strings/str_format.h"
#include "ortools/base/init_google.h"
#include "ortools/base/logging.h"
#include "ortools/sat/cp_model.h"
#include "ortools/sat/cp_model.pb.h"
#include "ortools/sat/cp_model_solver.h"

namespace operations_research {
namespace sat {

void ScheduleRequestsSat() {
  const int num_nurses = 5;
  const int num_days = 7;
  const int num_shifts = 3;

  std::vector<int> all_nurses(num_nurses);
  std::iota(all_nurses.begin(), all_nurses.end(), 0);

  std::vector<int> all_days(num_days);
  std::iota(all_days.begin(), all_days.end(), 0);

  std::vector<int> all_shifts(num_shifts);
  std::iota(all_shifts.begin(), all_shifts.end(), 0);

  std::vector<std::vector<std::vector<int64_t>>> shift_requests = {
      {
          {0, 0, 1},
          {0, 0, 0},
          {0, 0, 0},
          {0, 0, 0},
          {0, 0, 1},
          {0, 1, 0},
          {0, 0, 1},
      },
      {
          {0, 0, 0},
          {0, 0, 0},
          {0, 1, 0},
          {0, 1, 0},
          {1, 0, 0},
          {0, 0, 0},
          {0, 0, 1},
      },
      {
          {0, 1, 0},
          {0, 1, 0},
          {0, 0, 0},
          {1, 0, 0},
          {0, 0, 0},
          {0, 1, 0},
          {0, 0, 0},
      },
      {
          {0, 0, 1},
          {0, 0, 0},
          {1, 0, 0},
          {0, 1, 0},
          {0, 0, 0},
          {1, 0, 0},
          {0, 0, 0},
      },
      {
          {0, 0, 0},
          {0, 0, 1},
          {0, 1, 0},
          {0, 0, 0},
          {1, 0, 0},
          {0, 1, 0},
          {0, 0, 0},
      },
  };

  // Creates the model.
  CpModelBuilder cp_model;

  // Creates shift variables.
  // shifts[(n, d, s)]: nurse 'n' works shift 's' on day 'd'.
  std::map<std::tuple<int, int, int>, BoolVar> shifts;
  for (int n : all_nurses) {
    for (int d : all_days) {
      for (int s : all_shifts) {
        auto key = std::make_tuple(n, d, s);
        shifts[key] = cp_model.NewBoolVar().WithName(
            absl::StrFormat("shift_n%dd%ds%d", n, d, s));
      }
    }
  }

  // Each shift is assigned to exactly one nurse in the schedule period.
  for (int d : all_days) {
    for (int s : all_shifts) {
      std::vector<BoolVar> nurses;
      for (int n : all_nurses) {
        auto key = std::make_tuple(n, d, s);
        nurses.push_back(shifts[key]);
      }
      cp_model.AddExactlyOne(nurses);
    }
  }

  // Each nurse works at most one shift per day.
  for (int n : all_nurses) {
    for (int d : all_days) {
      std::vector<BoolVar> work;
      for (int s : all_shifts) {
        auto key = std::make_tuple(n, d, s);
        work.push_back(shifts[key]);
      }
      cp_model.AddAtMostOne(work);
    }
  }

  // Try to distribute the shifts evenly, so that each nurse works
  // min_shifts_per_nurse shifts. If this is not possible, because the total
  // number of shifts is not divisible by the number of nurses, some nurses will
  // be assigned one more shift.
  int min_shifts_per_nurse = (num_shifts * num_days) / num_nurses;
  int max_shifts_per_nurse;
  if ((num_shifts * num_days) % num_nurses == 0) {
    max_shifts_per_nurse = min_shifts_per_nurse;
  } else {
    max_shifts_per_nurse = min_shifts_per_nurse + 1;
  }
  for (int n : all_nurses) {
    LinearExpr num_worked_shifts;
    for (int d : all_days) {
      for (int s : all_shifts) {
        auto key = std::make_tuple(n, d, s);
        num_worked_shifts += shifts[key];
      }
    }
    cp_model.AddLessOrEqual(min_shifts_per_nurse, num_worked_shifts);
    cp_model.AddLessOrEqual(num_worked_shifts, max_shifts_per_nurse);
  }

  LinearExpr objective_expr;
  for (int n : all_nurses) {
    for (int d : all_days) {
      for (int s : all_shifts) {
        if (shift_requests[n][d][s] == 1) {
          auto key = std::make_tuple(n, d, s);
          objective_expr += shifts[key] * shift_requests[n][d][s];
        }
      }
    }
  }
  cp_model.Maximize(objective_expr);

  const CpSolverResponse response = Solve(cp_model.Build());

  if (response.status() == CpSolverStatus::OPTIMAL) {
    LOG(INFO) << "Solution:";
    for (int d : all_days) {
      LOG(INFO) << "Day " << std::to_string(d);
      for (int n : all_nurses) {
        for (int s : all_shifts) {
          auto key = std::make_tuple(n, d, s);
          if (SolutionIntegerValue(response, shifts[key]) == 1) {
            if (shift_requests[n][d][s] == 1) {
              LOG(INFO) << "  Nurse " << std::to_string(n) << " works shift "
                        << std::to_string(s) << " (requested).";
            } else {
              LOG(INFO) << "  Nurse " << std::to_string(n) << " works shift "
                        << std::to_string(s) << " (not requested).";
            }
          }
        }
      }
      LOG(INFO) << "";
    }
    LOG(INFO) << "Number of shift requests met = " << response.objective_value()
              << " (out of " << num_nurses * min_shifts_per_nurse << ")";
  } else {
    LOG(INFO) << "No optimal solution found !";
  }

  // Statistics.
  LOG(INFO) << "Statistics";
  LOG(INFO) << CpSolverResponseStats(response);
}

}  // namespace sat
}  // namespace operations_research

int main(int argc, char* argv[]) {
  InitGoogle(argv[0], &argc, &argv, true);
  absl::SetStderrThreshold(absl::LogSeverityAtLeast::kInfo);
  operations_research::sat::ScheduleRequestsSat();
  return EXIT_SUCCESS;
}
```

### Java

```java
package com.google.ortools.sat.samples;
import com.google.ortools.Loader;
import com.google.ortools.sat.CpModel;
import com.google.ortools.sat.CpSolver;
import com.google.ortools.sat.CpSolverStatus;
import com.google.ortools.sat.LinearExpr;
import com.google.ortools.sat.LinearExprBuilder;
import com.google.ortools.sat.Literal;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.IntStream;

/** Nurses problem with schedule requests. */
public class ScheduleRequestsSat {
  public static void main(String[] args) {
    Loader.loadNativeLibraries();
    final int numNurses = 5;
    final int numDays = 7;
    final int numShifts = 3;

    final int[] allNurses = IntStream.range(0, numNurses).toArray();
    final int[] allDays = IntStream.range(0, numDays).toArray();
    final int[] allShifts = IntStream.range(0, numShifts).toArray();

    final int[][][] shiftRequests = new int[][][] {
        {
            {0, 0, 1},
            {0, 0, 0},
            {0, 0, 0},
            {0, 0, 0},
            {0, 0, 1},
            {0, 1, 0},
            {0, 0, 1},
        },
        {
            {0, 0, 0},
            {0, 0, 0},
            {0, 1, 0},
            {0, 1, 0},
            {1, 0, 0},
            {0, 0, 0},
            {0, 0, 1},
        },
        {
            {0, 1, 0},
            {0, 1, 0},
            {0, 0, 0},
            {1, 0, 0},
            {0, 0, 0},
            {0, 1, 0},
            {0, 0, 0},
        },
        {
            {0, 0, 1},
            {0, 0, 0},
            {1, 0, 0},
            {0, 1, 0},
            {0, 0, 0},
            {1, 0, 0},
            {0, 0, 0},
        },
        {
            {0, 0, 0},
            {0, 0, 1},
            {0, 1, 0},
            {0, 0, 0},
            {1, 0, 0},
            {0, 1, 0},
            {0, 0, 0},
        },
    };

    // Creates the model.
    CpModel model = new CpModel();

    // Creates shift variables.
    // shifts[(n, d, s)]: nurse 'n' works shift 's' on day 'd'.
    Literal[][][] shifts = new Literal[numNurses][numDays][numShifts];
    for (int n : allNurses) {
      for (int d : allDays) {
        for (int s : allShifts) {
          shifts[n][d][s] = model.newBoolVar("shifts_n" + n + "d" + d + "s" + s);
        }
      }
    }

    // Each shift is assigned to exactly one nurse in the schedule period.
    for (int d : allDays) {
      for (int s : allShifts) {
        List<Literal> nurses = new ArrayList<>();
        for (int n : allNurses) {
          nurses.add(shifts[n][d][s]);
        }
        model.addExactlyOne(nurses);
      }
    }

    // Each nurse works at most one shift per day.
    for (int n : allNurses) {
      for (int d : allDays) {
        List<Literal> work = new ArrayList<>();
        for (int s : allShifts) {
          work.add(shifts[n][d][s]);
        }
        model.addAtMostOne(work);
      }
    }

    // Try to distribute the shifts evenly, so that each nurse works
    // minShiftsPerNurse shifts. If this is not possible, because the total
    // number of shifts is not divisible by the number of nurses, some nurses will
    // be assigned one more shift.
    int minShiftsPerNurse = (numShifts * numDays) / numNurses;
    int maxShiftsPerNurse;
    if ((numShifts * numDays) % numNurses == 0) {
      maxShiftsPerNurse = minShiftsPerNurse;
    } else {
      maxShiftsPerNurse = minShiftsPerNurse + 1;
    }
    for (int n : allNurses) {
      LinearExprBuilder numShiftsWorked = LinearExpr.newBuilder();
      for (int d : allDays) {
        for (int s : allShifts) {
          numShiftsWorked.add(shifts[n][d][s]);
        }
      }
      model.addLinearConstraint(numShiftsWorked, minShiftsPerNurse, maxShiftsPerNurse);
    }

    LinearExprBuilder obj = LinearExpr.newBuilder();
    for (int n : allNurses) {
      for (int d : allDays) {
        for (int s : allShifts) {
          obj.addTerm(shifts[n][d][s], shiftRequests[n][d][s]);
        }
      }
    }
    model.maximize(obj);

    // Creates a solver and solves the model.
    CpSolver solver = new CpSolver();
    CpSolverStatus status = solver.solve(model);

    if (status == CpSolverStatus.OPTIMAL || status == CpSolverStatus.FEASIBLE) {
      System.out.printf("Solution:%n");
      for (int d : allDays) {
        System.out.printf("Day %d%n", d);
        for (int n : allNurses) {
          for (int s : allShifts) {
            if (solver.booleanValue(shifts[n][d][s])) {
              if (shiftRequests[n][d][s] == 1) {
                System.out.printf("  Nurse %d works shift %d (requested).%n", n, s);
              } else {
                System.out.printf("  Nurse %d works shift %d (not requested).%n", n, s);
              }
            }
          }
        }
      }
      System.out.printf("Number of shift requests met = %f (out of %d)%n", solver.objectiveValue(),
          numNurses * minShiftsPerNurse);
    } else {
      System.out.printf("No optimal solution found !");
    }
    // Statistics.
    System.out.println("Statistics");
    System.out.printf("  conflicts: %d%n", solver.numConflicts());
    System.out.printf("  branches : %d%n", solver.numBranches());
    System.out.printf("  wall time: %f s%n", solver.wallTime());
  }

  private ScheduleRequestsSat() {}
}
```

### C#

```c#
using System;
using System.Collections.Generic;
using System.Linq;
using Google.OrTools.Sat;

public class ScheduleRequestsSat
{
    public static void Main(String[] args)
    {
        const int numNurses = 5;
        const int numDays = 7;
        const int numShifts = 3;

        int[] allNurses = Enumerable.Range(0, numNurses).ToArray();
        int[] allDays = Enumerable.Range(0, numDays).ToArray();
        int[] allShifts = Enumerable.Range(0, numShifts).ToArray();

        int[,,] shiftRequests = new int[,,] {
            {
                { 0, 0, 1 },
                { 0, 0, 0 },
                { 0, 0, 0 },
                { 0, 0, 0 },
                { 0, 0, 1 },
                { 0, 1, 0 },
                { 0, 0, 1 },
            },
            {
                { 0, 0, 0 },
                { 0, 0, 0 },
                { 0, 1, 0 },
                { 0, 1, 0 },
                { 1, 0, 0 },
                { 0, 0, 0 },
                { 0, 0, 1 },
            },
            {
                { 0, 1, 0 },
                { 0, 1, 0 },
                { 0, 0, 0 },
                { 1, 0, 0 },
                { 0, 0, 0 },
                { 0, 1, 0 },
                { 0, 0, 0 },
            },
            {
                { 0, 0, 1 },
                { 0, 0, 0 },
                { 1, 0, 0 },
                { 0, 1, 0 },
                { 0, 0, 0 },
                { 1, 0, 0 },
                { 0, 0, 0 },
            },
            {
                { 0, 0, 0 },
                { 0, 0, 1 },
                { 0, 1, 0 },
                { 0, 0, 0 },
                { 1, 0, 0 },
                { 0, 1, 0 },
                { 0, 0, 0 },
            },
        };

        // Creates the model.
        CpModel model = new CpModel();

        // Creates shift variables.
        // shifts[(n, d, s)]: nurse 'n' works shift 's' on day 'd'.
        Dictionary<Tuple<int, int, int>, IntVar> shifts = new Dictionary<Tuple<int, int, int>, IntVar>();
        foreach (int n in allNurses)
        {
            foreach (int d in allDays)
            {
                foreach (int s in allShifts)
                {
                    shifts.Add(Tuple.Create(n, d, s), model.NewBoolVar($"shifts_n{n}d{d}s{s}"));
                }
            }
        }

        // Each shift is assigned to exactly one nurse in the schedule period.
        foreach (int d in allDays)
        {
            foreach (int s in allShifts)
            {
                IntVar[] x = new IntVar[numNurses];
                foreach (int n in allNurses)
                {
                    var key = Tuple.Create(n, d, s);
                    x[n] = shifts[key];
                }
                model.Add(LinearExpr.Sum(x) == 1);
            }
        }

        // Each nurse works at most one shift per day.
        foreach (int n in allNurses)
        {
            foreach (int d in allDays)
            {
                IntVar[] x = new IntVar[numShifts];
                foreach (int s in allShifts)
                {
                    var key = Tuple.Create(n, d, s);
                    x[s] = shifts[key];
                }
                model.Add(LinearExpr.Sum(x) <= 1);
            }
        }

        // Try to distribute the shifts evenly, so that each nurse works
        // minShiftsPerNurse shifts. If this is not possible, because the total
        // number of shifts is not divisible by the number of nurses, some nurses will
        // be assigned one more shift.
        int minShiftsPerNurse = (numShifts * numDays) / numNurses;
        int maxShiftsPerNurse;
        if ((numShifts * numDays) % numNurses == 0)
        {
            maxShiftsPerNurse = minShiftsPerNurse;
        }
        else
        {
            maxShiftsPerNurse = minShiftsPerNurse + 1;
        }
        foreach (int n in allNurses)
        {
            IntVar[] numShiftsWorked = new IntVar[numDays * numShifts];
            foreach (int d in allDays)
            {
                foreach (int s in allShifts)
                {
                    var key = Tuple.Create(n, d, s);
                    numShiftsWorked[d * numShifts + s] = shifts[key];
                }
            }
            model.AddLinearConstraint(LinearExpr.Sum(numShiftsWorked), minShiftsPerNurse, maxShiftsPerNurse);
        }

        IntVar[] flatShifts = new IntVar[numNurses * numDays * numShifts];
        int[] flatShiftRequests = new int[numNurses * numDays * numShifts];
        foreach (int n in allNurses)
        {
            foreach (int d in allDays)
            {
                foreach (int s in allShifts)
                {
                    var key = Tuple.Create(n, d, s);
                    flatShifts[n * numDays * numShifts + d * numShifts + s] = shifts[key];
                    flatShiftRequests[n * numDays * numShifts + d * numShifts + s] = shiftRequests[n, d, s];
                }
            }
        }
        model.Maximize(LinearExpr.WeightedSum(flatShifts, flatShiftRequests));

        // Solve
        CpSolver solver = new CpSolver();
        CpSolverStatus status = solver.Solve(model);
        Console.WriteLine($"Solve status: {status}");

        if (status == CpSolverStatus.Optimal || status == CpSolverStatus.Feasible)
        {
            Console.WriteLine("Solution:");
            foreach (int d in allDays)
            {
                Console.WriteLine($"Day {d}");
                foreach (int n in allNurses)
                {
                    bool isWorking = false;
                    foreach (int s in allShifts)
                    {
                        var key = Tuple.Create(n, d, s);
                        if (solver.Value(shifts[key]) == 1L)
                        {
                            if (shiftRequests[n, d, s] == 1)
                            {
                                Console.WriteLine($"  Nurse {n} work shift {s} (requested).");
                            }
                            else
                            {
                                Console.WriteLine($"  Nurse {n} work shift {s} (not requested).");
                            }
                        }
                    }
                }
            }
            Console.WriteLine(
                $"Number of shift requests met = {solver.ObjectiveValue} (out of {numNurses * minShiftsPerNurse}).");
        }
        else
        {
            Console.WriteLine("No solution found.");
        }

        Console.WriteLine("Statistics");
        Console.WriteLine($"  conflicts: {solver.NumConflicts()}");
        Console.WriteLine($"  branches : {solver.NumBranches()}");
        Console.WriteLine($"  wall time: {solver.WallTime()}s");
    }
}
```

# CP-SAT Solver

OR-Tools offers two main tools for solving integer programming problems:

- [MPSolver](https://developers.google.com/optimization/lp/mpsolver), described in a previous section.
- The CP-SAT solver, which we describe next.

For an example that solves an integer programming problem using both the CP-SAT
solver and the MPSolver wrapper, see
[Solving an Assignment Problem](https://developers.google.com/optimization/assignment/assignment_example).

> [!NOTE]
> **Note:** To increase computational speed, the CP-SAT solver works over the integers. This means you must define your optimization problem using integers only. If you begin with a problem that has constraints with non-integer terms, you need to first multiply those constraints by a sufficiently large integer so that all terms are integers. See [Solving an Optimization Problem](https://developers.google.com/optimization/cp/integer_opt_cp) for an example.

The following sections present examples that show how to use the CP-SAT solver.

## Example: finding a feasible solution

Let's start with a simple example problem in which there are:

- Three variables, x, y, and z, each of which can take on the values: 0, 1, or 2.
- One constraint: `x != y`

We'll start by showing how to use the CP-SAT solver to find a single feasible
solution in all of the supported languages. While finding a feasible solution is
trivial in this case, in more complex constraint programming problems it can be
very difficult to determine whether there is a feasible solution.

For an example of finding an optimal solution to a CP problem, see
[Solving an Optimization Problem](https://developers.google.com/optimization/cp/cp_example).

### Import the libraries

The following code imports the required library.

### Python

```python
from ortools.sat.python import cp_model
```

### C++

```c++
#include <stdlib.h>

#include "absl/base/log_severity.h"
#include "absl/log/globals.h"
#include "ortools/base/init_google.h"
#include "ortools/base/logging.h"
#include "ortools/sat/cp_model.h"
#include "ortools/sat/cp_model.pb.h"
#include "ortools/sat/cp_model_solver.h"
#include "ortools/util/sorted_interval_list.h"
```

### Java

```java
import com.google.ortools.Loader;
import com.google.ortools.sat.CpModel;
import com.google.ortools.sat.CpSolver;
import com.google.ortools.sat.CpSolverStatus;
import com.google.ortools.sat.IntVar;
```

### C#

```c#
using System;
using Google.OrTools.Sat;
```

### Declare the model

The following code declares the CP-SAT model.

### Python

```python
model = cp_model.CpModel()
```

### C++

```c++
CpModelBuilder cp_model;
```

### Java

```java
CpModel model = new CpModel();
```

### C#

```c#
CpModel model = new CpModel();
```

### Create the variables

The following code creates the variables for the problem.

### Python

```python
num_vals = 3
x = model.new_int_var(0, num_vals - 1, "x")
y = model.new_int_var(0, num_vals - 1, "y")
z = model.new_int_var(0, num_vals - 1, "z")
```

### C++

```c++
const Domain domain(0, 2);
const IntVar x = cp_model.NewIntVar(domain).WithName("x");
const IntVar y = cp_model.NewIntVar(domain).WithName("y");
const IntVar z = cp_model.NewIntVar(domain).WithName("z");
```

### Java

```java
int numVals = 3;

IntVar x = model.newIntVar(0, numVals - 1, "x");
IntVar y = model.newIntVar(0, numVals - 1, "y");
IntVar z = model.newIntVar(0, numVals - 1, "z");
```

### C#

```c#
int num_vals = 3;

IntVar x = model.NewIntVar(0, num_vals - 1, "x");
IntVar y = model.NewIntVar(0, num_vals - 1, "y");
IntVar z = model.NewIntVar(0, num_vals - 1, "z");
```

The solver creates three variables, x, y, and z, each of which can take on the
values 0, 1, or 2.

### Create the constraint

The following code creates the constraint `x != y`.

### Python

```python
model.add(x != y)
```

### C++

```c++
cp_model.AddNotEqual(x, y);
```

### Java

```java
model.addDifferent(x, y);
```

### C#

```c#
model.Add(x != y);
```

### Call the solver

The following code calls the solver.

### Python

```python
solver = cp_model.CpSolver()
status = solver.solve(model)
```

### C++

```c++
const CpSolverResponse response = Solve(cp_model.Build());
```

### Java

```java
CpSolver solver = new CpSolver();
CpSolverStatus status = solver.solve(model);
```

### C#

```c#
CpSolver solver = new CpSolver();
CpSolverStatus status = solver.Solve(model);
```

### CP-SAT return values

The CP-SAT solver returns one of the status values shown in the table below. In
this example, the value returned is `OPTIMAL`.

| Status | Description |
|---|---|
| `OPTIMAL` | An optimal feasible solution was found. |
| `FEASIBLE` | A feasible solution was found, but we don't know if it's optimal. |
| `INFEASIBLE` | The problem was proven infeasible. |
| `MODEL_INVALID` | The given CpModelProto didn't pass the validation step. You can get a detailed error by calling `ValidateCpModel(model_proto)`. |
| `UNKNOWN` | The status of the model is unknown because no solution was found (or the problem was not proven INFEASIBLE) before something caused the solver to stop, such as a [time limit](https://developers.google.com/optimization/cp/cp_tasks#time-limit), a memory limit, or a custom limit set by the user. |

These are defined in
[cp_model.proto](https://github.com/google/or-tools/blob/stable/ortools/sat/cp_model.proto).

### Display the first solution

The following code displays the first feasible solution found by the solver.
Note that the code checks whether the value of the `status` is `FEASIBLE` or
`OPTIMAL`.

### Python

```python
if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print(f"x = {solver.value(x)}")
    print(f"y = {solver.value(y)}")
    print(f"z = {solver.value(z)}")
else:
    print("No solution found.")
```

### C++

```c++
if (response.status() == CpSolverStatus::OPTIMAL ||
    response.status() == CpSolverStatus::FEASIBLE) {
  // Get the value of x in the solution.
  LOG(INFO) << "x = " << SolutionIntegerValue(response, x);
  LOG(INFO) << "y = " << SolutionIntegerValue(response, y);
  LOG(INFO) << "z = " << SolutionIntegerValue(response, z);
} else {
  LOG(INFO) << "No solution found.";
}
```

### Java

```java
if (status == CpSolverStatus.OPTIMAL || status == CpSolverStatus.FEASIBLE) {
  System.out.println("x = " + solver.value(x));
  System.out.println("y = " + solver.value(y));
  System.out.println("z = " + solver.value(z));
} else {
  System.out.println("No solution found.");
}
```

### C#

```c#
if (status == CpSolverStatus.Optimal || status == CpSolverStatus.Feasible)
{
    Console.WriteLine("x = " + solver.Value(x));
    Console.WriteLine("y = " + solver.Value(y));
    Console.WriteLine("z = " + solver.Value(z));
}
else
{
    Console.WriteLine("No solution found.");
}
```

### Run the program

The complete programs are shown the [next section](https://developers.google.com/optimization/cp/cp_solver#first_sol_program).
When you run a program, it returns the first solution found by the solver:

```
x = 1
y = 0
z = 0
```

### Complete programs

The complete programs are shown below.

### Python

```python
"""Simple solve."""
from ortools.sat.python import cp_model



def simple_sat_program():
    """Minimal CP-SAT example to showcase calling the solver."""
    # Creates the model.
    model = cp_model.CpModel()

    # Creates the variables.
    num_vals = 3
    x = model.new_int_var(0, num_vals - 1, "x")
    y = model.new_int_var(0, num_vals - 1, "y")
    z = model.new_int_var(0, num_vals - 1, "z")

    # Creates the constraints.
    model.add(x != y)

    # Creates a solver and solves the model.
    solver = cp_model.CpSolver()
    status = solver.solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f"x = {solver.value(x)}")
        print(f"y = {solver.value(y)}")
        print(f"z = {solver.value(z)}")
    else:
        print("No solution found.")


simple_sat_program()
```

### C++

```c++
#include <stdlib.h>

#include "absl/base/log_severity.h"
#include "absl/log/globals.h"
#include "ortools/base/init_google.h"
#include "ortools/base/logging.h"
#include "ortools/sat/cp_model.h"
#include "ortools/sat/cp_model.pb.h"
#include "ortools/sat/cp_model_solver.h"
#include "ortools/util/sorted_interval_list.h"

namespace operations_research {
namespace sat {

void SimpleSatProgram() {
  CpModelBuilder cp_model;

  const Domain domain(0, 2);
  const IntVar x = cp_model.NewIntVar(domain).WithName("x");
  const IntVar y = cp_model.NewIntVar(domain).WithName("y");
  const IntVar z = cp_model.NewIntVar(domain).WithName("z");

  cp_model.AddNotEqual(x, y);

  // Solving part.
  const CpSolverResponse response = Solve(cp_model.Build());

  if (response.status() == CpSolverStatus::OPTIMAL ||
      response.status() == CpSolverStatus::FEASIBLE) {
    // Get the value of x in the solution.
    LOG(INFO) << "x = " << SolutionIntegerValue(response, x);
    LOG(INFO) << "y = " << SolutionIntegerValue(response, y);
    LOG(INFO) << "z = " << SolutionIntegerValue(response, z);
  } else {
    LOG(INFO) << "No solution found.";
  }
}

}  // namespace sat
}  // namespace operations_research

int main(int argc, char* argv[]) {
  InitGoogle(argv[0], &argc, &argv, true);
  absl::SetStderrThreshold(absl::LogSeverityAtLeast::kInfo);
  operations_research::sat::SimpleSatProgram();
  return EXIT_SUCCESS;
}
```

### Java

```java
package com.google.ortools.sat.samples;
import com.google.ortools.Loader;
import com.google.ortools.sat.CpModel;
import com.google.ortools.sat.CpSolver;
import com.google.ortools.sat.CpSolverStatus;
import com.google.ortools.sat.IntVar;

/** Minimal CP-SAT example to showcase calling the solver. */
public final class SimpleSatProgram {
  public static void main(String[] args) throws Exception {
    Loader.loadNativeLibraries();
    // Create the model.
    CpModel model = new CpModel();

    // Create the variables.
    int numVals = 3;

    IntVar x = model.newIntVar(0, numVals - 1, "x");
    IntVar y = model.newIntVar(0, numVals - 1, "y");
    IntVar z = model.newIntVar(0, numVals - 1, "z");

    // Create the constraints.
    model.addDifferent(x, y);

    // Create a solver and solve the model.
    CpSolver solver = new CpSolver();
    CpSolverStatus status = solver.solve(model);

    if (status == CpSolverStatus.OPTIMAL || status == CpSolverStatus.FEASIBLE) {
      System.out.println("x = " + solver.value(x));
      System.out.println("y = " + solver.value(y));
      System.out.println("z = " + solver.value(z));
    } else {
      System.out.println("No solution found.");
    }
  }

  private SimpleSatProgram() {}
}
```

### C#

```c#
using System;
using Google.OrTools.Sat;

public class SimpleSatProgram
{
    static void Main()
    {
        // Creates the model.
        CpModel model = new CpModel();

        // Creates the variables.
        int num_vals = 3;

        IntVar x = model.NewIntVar(0, num_vals - 1, "x");
        IntVar y = model.NewIntVar(0, num_vals - 1, "y");
        IntVar z = model.NewIntVar(0, num_vals - 1, "z");

        // Creates the constraints.
        model.Add(x != y);

        // Creates a solver and solves the model.
        CpSolver solver = new CpSolver();
        CpSolverStatus status = solver.Solve(model);

        if (status == CpSolverStatus.Optimal || status == CpSolverStatus.Feasible)
        {
            Console.WriteLine("x = " + solver.Value(x));
            Console.WriteLine("y = " + solver.Value(y));
            Console.WriteLine("z = " + solver.Value(z));
        }
        else
        {
            Console.WriteLine("No solution found.");
        }
    }
}
```

## Finding all solutions

Next, we'll show how to modify the [program above](https://developers.google.com/optimization/cp/cp_solver#first_sol_program) to find
all feasible solutions.

The main addition to the program is a **solution printer** a callback that you
pass to the solver, which displays each solution as it is found.

### Add the solution printer

The following code creates the solution printer.

### Python

```python
class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, variables: list[cp_model.IntVar]):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0

    def on_solution_callback(self) -> None:
        self.__solution_count += 1
        for v in self.__variables:
            print(f"{v}={self.value(v)}", end=" ")
        print()

    @property
    def solution_count(self) -> int:
        return self.__solution_count
```

### C++

```c++
Model model;

int num_solutions = 0;
model.Add(NewFeasibleSolutionObserver([&](const CpSolverResponse& r) {
  LOG(INFO) << "Solution " << num_solutions;
  LOG(INFO) << "  x = " << SolutionIntegerValue(r, x);
  LOG(INFO) << "  y = " << SolutionIntegerValue(r, y);
  LOG(INFO) << "  z = " << SolutionIntegerValue(r, z);
  num_solutions++;
}));
```

### Java

```java
static class VarArraySolutionPrinter extends CpSolverSolutionCallback {
  public VarArraySolutionPrinter(IntVar[] variables) {
    variableArray = variables;
  }

  @Override
  public void onSolutionCallback() {
    System.out.printf("Solution #%d: time = %.02f s%n", solutionCount, wallTime());
    for (IntVar v : variableArray) {
      System.out.printf("  %s = %d%n", v.getName(), value(v));
    }
    solutionCount++;
  }

  public int getSolutionCount() {
    return solutionCount;
  }

  private int solutionCount;
  private final IntVar[] variableArray;
}
```

### C#

```c#
public class VarArraySolutionPrinter : CpSolverSolutionCallback
{
    public VarArraySolutionPrinter(IntVar[] variables)
    {
        variables_ = variables;
    }

    public override void OnSolutionCallback()
    {
        {
            Console.WriteLine(String.Format("Solution #{0}: time = {1:F2} s", solution_count_, WallTime()));
            foreach (IntVar v in variables_)
            {
                Console.WriteLine(String.Format("  {0} = {1}", v.ToString(), Value(v)));
            }
            solution_count_++;
        }
    }

    public int SolutionCount()
    {
        return solution_count_;
    }

    private int solution_count_;
    private IntVar[] variables_;
}
```

### Call the solver

The following code calls the solver, and passes the solution printer to it.

### Python

```python
solver = cp_model.CpSolver()
solution_printer = VarArraySolutionPrinter([x, y, z])
# Enumerate all solutions.
solver.parameters.enumerate_all_solutions = True
# Solve.
status = solver.solve(model, solution_printer)
```

### C++

```c++
SatParameters parameters;
parameters.set_enumerate_all_solutions(true);
model.Add(NewSatParameters(parameters));
const CpSolverResponse response = SolveCpModel(cp_model.Build(), &model);
```

### Java

```java
CpSolver solver = new CpSolver();
VarArraySolutionPrinter cb = new VarArraySolutionPrinter(new IntVar[] {x, y, z});
// Tell the solver to enumerate all solutions.
solver.getParameters().setEnumerateAllSolutions(true);
// And solve.
CpSolverStatus unusedStatus = solver.solve(model, cb);
```

### C#

```c#
CpSolver solver = new CpSolver();
VarArraySolutionPrinter cb = new VarArraySolutionPrinter(new IntVar[] { x, y, z });
// Search for all solutions.
solver.StringParameters = "enumerate_all_solutions:true";
// And solve.
solver.Solve(model, cb);
```

### Run the program

The complete program is shown in the [next section](https://developers.google.com/optimization/cp/cp_solver#all_solutions_program).
When you run the program, it displays all 18 feasible solutions:

```
x=1 y=0 z=0
x=2 y=0 z=0
x=2 y=1 z=0
x=2 y=1 z=1
x=2 y=1 z=2
x=2 y=0 z=2
x=2 y=0 z=1
x=1 y=0 z=1
x=0 y=1 z=1
x=0 y=1 z=2
x=0 y=2 z=2
x=1 y=2 z=2
x=1 y=2 z=1
x=1 y=2 z=0
x=0 y=2 z=0
x=0 y=1 z=0
x=0 y=2 z=1
x=1 y=0 z=2
Status = FEASIBLE
```

### Complete programs

The complete programs are shown below.

### Python

```python
from ortools.sat.python import cp_model


class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, variables: list[cp_model.IntVar]):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0

    def on_solution_callback(self) -> None:
        self.__solution_count += 1
        for v in self.__variables:
            print(f"{v}={self.value(v)}", end=" ")
        print()

    @property
    def solution_count(self) -> int:
        return self.__solution_count


def search_for_all_solutions_sample_sat():
    """Showcases calling the solver to search for all solutions."""
    # Creates the model.
    model = cp_model.CpModel()

    # Creates the variables.
    num_vals = 3
    x = model.new_int_var(0, num_vals - 1, "x")
    y = model.new_int_var(0, num_vals - 1, "y")
    z = model.new_int_var(0, num_vals - 1, "z")

    # Create the constraints.
    model.add(x != y)

    # Create a solver and solve.
    solver = cp_model.CpSolver()
    solution_printer = VarArraySolutionPrinter([x, y, z])
    # Enumerate all solutions.
    solver.parameters.enumerate_all_solutions = True
    # Solve.
    status = solver.solve(model, solution_printer)

    print(f"Status = {solver.status_name(status)}")
    print(f"Number of solutions found: {solution_printer.solution_count}")


search_for_all_solutions_sample_sat()
```

### C++

```c++
#include <stdlib.h>

#include "absl/base/log_severity.h"
#include "absl/log/globals.h"
#include "ortools/base/init_google.h"
#include "ortools/base/logging.h"
#include "ortools/sat/cp_model.h"
#include "ortools/sat/cp_model.pb.h"
#include "ortools/sat/cp_model_solver.h"
#include "ortools/sat/model.h"
#include "ortools/sat/sat_parameters.pb.h"
#include "ortools/util/sorted_interval_list.h"

namespace operations_research {
namespace sat {

void SearchAllSolutionsSampleSat() {
  CpModelBuilder cp_model;

  const Domain domain(0, 2);
  const IntVar x = cp_model.NewIntVar(domain).WithName("x");
  const IntVar y = cp_model.NewIntVar(domain).WithName("y");
  const IntVar z = cp_model.NewIntVar(domain).WithName("z");

  cp_model.AddNotEqual(x, y);

  Model model;

  int num_solutions = 0;
  model.Add(NewFeasibleSolutionObserver([&](const CpSolverResponse& r) {
    LOG(INFO) << "Solution " << num_solutions;
    LOG(INFO) << "  x = " << SolutionIntegerValue(r, x);
    LOG(INFO) << "  y = " << SolutionIntegerValue(r, y);
    LOG(INFO) << "  z = " << SolutionIntegerValue(r, z);
    num_solutions++;
  }));

  // Tell the solver to enumerate all solutions.
  SatParameters parameters;
  parameters.set_enumerate_all_solutions(true);
  model.Add(NewSatParameters(parameters));
  const CpSolverResponse response = SolveCpModel(cp_model.Build(), &model);

  LOG(INFO) << "Number of solutions found: " << num_solutions;
}

}  // namespace sat
}  // namespace operations_research

int main(int argc, char* argv[]) {
  InitGoogle(argv[0], &argc, &argv, true);
  absl::SetStderrThreshold(absl::LogSeverityAtLeast::kInfo);
  operations_research::sat::SearchAllSolutionsSampleSat();
  return EXIT_SUCCESS;
}
```

### Java

```java
package com.google.ortools.sat.samples;

import com.google.ortools.Loader;
import com.google.ortools.sat.CpModel;
import com.google.ortools.sat.CpSolver;
import com.google.ortools.sat.CpSolverSolutionCallback;
import com.google.ortools.sat.CpSolverStatus;
import com.google.ortools.sat.IntVar;

/** Code sample that solves a model and displays all solutions. */
public class SearchForAllSolutionsSampleSat {
  static class VarArraySolutionPrinter extends CpSolverSolutionCallback {
    public VarArraySolutionPrinter(IntVar[] variables) {
      variableArray = variables;
    }

    @Override
    public void onSolutionCallback() {
      System.out.printf("Solution #%d: time = %.02f s%n", solutionCount, wallTime());
      for (IntVar v : variableArray) {
        System.out.printf("  %s = %d%n", v.getName(), value(v));
      }
      solutionCount++;
    }

    public int getSolutionCount() {
      return solutionCount;
    }

    private int solutionCount;
    private final IntVar[] variableArray;
  }

  public static void main(String[] args) throws Exception {
    Loader.loadNativeLibraries();
    // Create the model.
    CpModel model = new CpModel();

    // Create the variables.
    int numVals = 3;

    IntVar x = model.newIntVar(0, numVals - 1, "x");
    IntVar y = model.newIntVar(0, numVals - 1, "y");
    IntVar z = model.newIntVar(0, numVals - 1, "z");

    // Create the constraints.
    model.addDifferent(x, y);

    // Create a solver and solve the model.
    CpSolver solver = new CpSolver();
    VarArraySolutionPrinter cb = new VarArraySolutionPrinter(new IntVar[] {x, y, z});
    // Tell the solver to enumerate all solutions.
    solver.getParameters().setEnumerateAllSolutions(true);
    // And solve.
    CpSolverStatus unusedStatus = solver.solve(model, cb);

    System.out.println(cb.getSolutionCount() + " solutions found.");
  }
}
```

### C#

```c#
using System;
using Google.OrTools.Sat;

public class VarArraySolutionPrinter : CpSolverSolutionCallback
{
    public VarArraySolutionPrinter(IntVar[] variables)
    {
        variables_ = variables;
    }

    public override void OnSolutionCallback()
    {
        {
            Console.WriteLine(String.Format("Solution #{0}: time = {1:F2} s", solution_count_, WallTime()));
            foreach (IntVar v in variables_)
            {
                Console.WriteLine(String.Format("  {0} = {1}", v.ToString(), Value(v)));
            }
            solution_count_++;
        }
    }

    public int SolutionCount()
    {
        return solution_count_;
    }

    private int solution_count_;
    private IntVar[] variables_;
}

public class SearchForAllSolutionsSampleSat
{
    static void Main()
    {
        // Creates the model.
        CpModel model = new CpModel();

        // Creates the variables.
        int num_vals = 3;

        IntVar x = model.NewIntVar(0, num_vals - 1, "x");
        IntVar y = model.NewIntVar(0, num_vals - 1, "y");
        IntVar z = model.NewIntVar(0, num_vals - 1, "z");

        // Adds a different constraint.
        model.Add(x != y);

        // Creates a solver and solves the model.
        CpSolver solver = new CpSolver();
        VarArraySolutionPrinter cb = new VarArraySolutionPrinter(new IntVar[] { x, y, z });
        // Search for all solutions.
        solver.StringParameters = "enumerate_all_solutions:true";
        // And solve.
        solver.Solve(model, cb);

        Console.WriteLine($"Number of solutions found: {cb.SolutionCount()}");
    }
}
```

# CP-SAT Solver

OR-Tools offers two main tools for solving integer programming problems:

- [MPSolver](https://developers.google.com/optimization/lp/mpsolver), described in a previous section.
- The CP-SAT solver, which we describe next.

For an example that solves an integer programming problem using both the CP-SAT
solver and the MPSolver wrapper, see
[Solving an Assignment Problem](https://developers.google.com/optimization/assignment/assignment_example).

> [!NOTE]
> **Note:** To increase computational speed, the CP-SAT solver works over the integers. This means you must define your optimization problem using integers only. If you begin with a problem that has constraints with non-integer terms, you need to first multiply those constraints by a sufficiently large integer so that all terms are integers. See [Solving an Optimization Problem](https://developers.google.com/optimization/cp/integer_opt_cp) for an example.

The following sections present examples that show how to use the CP-SAT solver.

## Example: finding a feasible solution

Let's start with a simple example problem in which there are:

- Three variables, x, y, and z, each of which can take on the values: 0, 1, or 2.
- One constraint: `x != y`

We'll start by showing how to use the CP-SAT solver to find a single feasible
solution in all of the supported languages. While finding a feasible solution is
trivial in this case, in more complex constraint programming problems it can be
very difficult to determine whether there is a feasible solution.

For an example of finding an optimal solution to a CP problem, see
[Solving an Optimization Problem](https://developers.google.com/optimization/cp/cp_example).

### Import the libraries

The following code imports the required library.

### Python

```python
from ortools.sat.python import cp_model
```

### C++

```c++
#include <stdlib.h>

#include "absl/base/log_severity.h"
#include "absl/log/globals.h"
#include "ortools/base/init_google.h"
#include "ortools/base/logging.h"
#include "ortools/sat/cp_model.h"
#include "ortools/sat/cp_model.pb.h"
#include "ortools/sat/cp_model_solver.h"
#include "ortools/util/sorted_interval_list.h"
```

### Java

```java
import com.google.ortools.Loader;
import com.google.ortools.sat.CpModel;
import com.google.ortools.sat.CpSolver;
import com.google.ortools.sat.CpSolverStatus;
import com.google.ortools.sat.IntVar;
```

### C#

```c#
using System;
using Google.OrTools.Sat;
```

### Declare the model

The following code declares the CP-SAT model.

### Python

```python
model = cp_model.CpModel()
```

### C++

```c++
CpModelBuilder cp_model;
```

### Java

```java
CpModel model = new CpModel();
```

### C#

```c#
CpModel model = new CpModel();
```

### Create the variables

The following code creates the variables for the problem.

### Python

```python
num_vals = 3
x = model.new_int_var(0, num_vals - 1, "x")
y = model.new_int_var(0, num_vals - 1, "y")
z = model.new_int_var(0, num_vals - 1, "z")
```

### C++

```c++
const Domain domain(0, 2);
const IntVar x = cp_model.NewIntVar(domain).WithName("x");
const IntVar y = cp_model.NewIntVar(domain).WithName("y");
const IntVar z = cp_model.NewIntVar(domain).WithName("z");
```

### Java

```java
int numVals = 3;

IntVar x = model.newIntVar(0, numVals - 1, "x");
IntVar y = model.newIntVar(0, numVals - 1, "y");
IntVar z = model.newIntVar(0, numVals - 1, "z");
```

### C#

```c#
int num_vals = 3;

IntVar x = model.NewIntVar(0, num_vals - 1, "x");
IntVar y = model.NewIntVar(0, num_vals - 1, "y");
IntVar z = model.NewIntVar(0, num_vals - 1, "z");
```

The solver creates three variables, x, y, and z, each of which can take on the
values 0, 1, or 2.

### Create the constraint

The following code creates the constraint `x != y`.

### Python

```python
model.add(x != y)
```

### C++

```c++
cp_model.AddNotEqual(x, y);
```

### Java

```java
model.addDifferent(x, y);
```

### C#

```c#
model.Add(x != y);
```

### Call the solver

The following code calls the solver.

### Python

```python
solver = cp_model.CpSolver()
status = solver.solve(model)
```

### C++

```c++
const CpSolverResponse response = Solve(cp_model.Build());
```

### Java

```java
CpSolver solver = new CpSolver();
CpSolverStatus status = solver.solve(model);
```

### C#

```c#
CpSolver solver = new CpSolver();
CpSolverStatus status = solver.Solve(model);
```

### CP-SAT return values

The CP-SAT solver returns one of the status values shown in the table below. In
this example, the value returned is `OPTIMAL`.

| Status | Description |
|---|---|
| `OPTIMAL` | An optimal feasible solution was found. |
| `FEASIBLE` | A feasible solution was found, but we don't know if it's optimal. |
| `INFEASIBLE` | The problem was proven infeasible. |
| `MODEL_INVALID` | The given CpModelProto didn't pass the validation step. You can get a detailed error by calling `ValidateCpModel(model_proto)`. |
| `UNKNOWN` | The status of the model is unknown because no solution was found (or the problem was not proven INFEASIBLE) before something caused the solver to stop, such as a [time limit](https://developers.google.com/optimization/cp/cp_tasks#time-limit), a memory limit, or a custom limit set by the user. |

These are defined in
[cp_model.proto](https://github.com/google/or-tools/blob/stable/ortools/sat/cp_model.proto).

### Display the first solution

The following code displays the first feasible solution found by the solver.
Note that the code checks whether the value of the `status` is `FEASIBLE` or
`OPTIMAL`.

### Python

```python
if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print(f"x = {solver.value(x)}")
    print(f"y = {solver.value(y)}")
    print(f"z = {solver.value(z)}")
else:
    print("No solution found.")
```

### C++

```c++
if (response.status() == CpSolverStatus::OPTIMAL ||
    response.status() == CpSolverStatus::FEASIBLE) {
  // Get the value of x in the solution.
  LOG(INFO) << "x = " << SolutionIntegerValue(response, x);
  LOG(INFO) << "y = " << SolutionIntegerValue(response, y);
  LOG(INFO) << "z = " << SolutionIntegerValue(response, z);
} else {
  LOG(INFO) << "No solution found.";
}
```

### Java

```java
if (status == CpSolverStatus.OPTIMAL || status == CpSolverStatus.FEASIBLE) {
  System.out.println("x = " + solver.value(x));
  System.out.println("y = " + solver.value(y));
  System.out.println("z = " + solver.value(z));
} else {
  System.out.println("No solution found.");
}
```

### C#

```c#
if (status == CpSolverStatus.Optimal || status == CpSolverStatus.Feasible)
{
    Console.WriteLine("x = " + solver.Value(x));
    Console.WriteLine("y = " + solver.Value(y));
    Console.WriteLine("z = " + solver.Value(z));
}
else
{
    Console.WriteLine("No solution found.");
}
```

### Run the program

The complete programs are shown the [next section](https://developers.google.com/optimization/cp/cp_solver#first_sol_program).
When you run a program, it returns the first solution found by the solver:

```
x = 1
y = 0
z = 0
```

### Complete programs

The complete programs are shown below.

### Python

```python
"""Simple solve."""
from ortools.sat.python import cp_model



def simple_sat_program():
    """Minimal CP-SAT example to showcase calling the solver."""
    # Creates the model.
    model = cp_model.CpModel()

    # Creates the variables.
    num_vals = 3
    x = model.new_int_var(0, num_vals - 1, "x")
    y = model.new_int_var(0, num_vals - 1, "y")
    z = model.new_int_var(0, num_vals - 1, "z")

    # Creates the constraints.
    model.add(x != y)

    # Creates a solver and solves the model.
    solver = cp_model.CpSolver()
    status = solver.solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f"x = {solver.value(x)}")
        print(f"y = {solver.value(y)}")
        print(f"z = {solver.value(z)}")
    else:
        print("No solution found.")


simple_sat_program()
```

### C++

```c++
#include <stdlib.h>

#include "absl/base/log_severity.h"
#include "absl/log/globals.h"
#include "ortools/base/init_google.h"
#include "ortools/base/logging.h"
#include "ortools/sat/cp_model.h"
#include "ortools/sat/cp_model.pb.h"
#include "ortools/sat/cp_model_solver.h"
#include "ortools/util/sorted_interval_list.h"

namespace operations_research {
namespace sat {

void SimpleSatProgram() {
  CpModelBuilder cp_model;

  const Domain domain(0, 2);
  const IntVar x = cp_model.NewIntVar(domain).WithName("x");
  const IntVar y = cp_model.NewIntVar(domain).WithName("y");
  const IntVar z = cp_model.NewIntVar(domain).WithName("z");

  cp_model.AddNotEqual(x, y);

  // Solving part.
  const CpSolverResponse response = Solve(cp_model.Build());

  if (response.status() == CpSolverStatus::OPTIMAL ||
      response.status() == CpSolverStatus::FEASIBLE) {
    // Get the value of x in the solution.
    LOG(INFO) << "x = " << SolutionIntegerValue(response, x);
    LOG(INFO) << "y = " << SolutionIntegerValue(response, y);
    LOG(INFO) << "z = " << SolutionIntegerValue(response, z);
  } else {
    LOG(INFO) << "No solution found.";
  }
}

}  // namespace sat
}  // namespace operations_research

int main(int argc, char* argv[]) {
  InitGoogle(argv[0], &argc, &argv, true);
  absl::SetStderrThreshold(absl::LogSeverityAtLeast::kInfo);
  operations_research::sat::SimpleSatProgram();
  return EXIT_SUCCESS;
}
```

### Java

```java
package com.google.ortools.sat.samples;
import com.google.ortools.Loader;
import com.google.ortools.sat.CpModel;
import com.google.ortools.sat.CpSolver;
import com.google.ortools.sat.CpSolverStatus;
import com.google.ortools.sat.IntVar;

/** Minimal CP-SAT example to showcase calling the solver. */
public final class SimpleSatProgram {
  public static void main(String[] args) throws Exception {
    Loader.loadNativeLibraries();
    // Create the model.
    CpModel model = new CpModel();

    // Create the variables.
    int numVals = 3;

    IntVar x = model.newIntVar(0, numVals - 1, "x");
    IntVar y = model.newIntVar(0, numVals - 1, "y");
    IntVar z = model.newIntVar(0, numVals - 1, "z");

    // Create the constraints.
    model.addDifferent(x, y);

    // Create a solver and solve the model.
    CpSolver solver = new CpSolver();
    CpSolverStatus status = solver.solve(model);

    if (status == CpSolverStatus.OPTIMAL || status == CpSolverStatus.FEASIBLE) {
      System.out.println("x = " + solver.value(x));
      System.out.println("y = " + solver.value(y));
      System.out.println("z = " + solver.value(z));
    } else {
      System.out.println("No solution found.");
    }
  }

  private SimpleSatProgram() {}
}
```

### C#

```c#
using System;
using Google.OrTools.Sat;

public class SimpleSatProgram
{
    static void Main()
    {
        // Creates the model.
        CpModel model = new CpModel();

        // Creates the variables.
        int num_vals = 3;

        IntVar x = model.NewIntVar(0, num_vals - 1, "x");
        IntVar y = model.NewIntVar(0, num_vals - 1, "y");
        IntVar z = model.NewIntVar(0, num_vals - 1, "z");

        // Creates the constraints.
        model.Add(x != y);

        // Creates a solver and solves the model.
        CpSolver solver = new CpSolver();
        CpSolverStatus status = solver.Solve(model);

        if (status == CpSolverStatus.Optimal || status == CpSolverStatus.Feasible)
        {
            Console.WriteLine("x = " + solver.Value(x));
            Console.WriteLine("y = " + solver.Value(y));
            Console.WriteLine("z = " + solver.Value(z));
        }
        else
        {
            Console.WriteLine("No solution found.");
        }
    }
}
```

## Finding all solutions

Next, we'll show how to modify the [program above](https://developers.google.com/optimization/cp/cp_solver#first_sol_program) to find
all feasible solutions.

The main addition to the program is a **solution printer** a callback that you
pass to the solver, which displays each solution as it is found.

### Add the solution printer

The following code creates the solution printer.

### Python

```python
class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, variables: list[cp_model.IntVar]):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0

    def on_solution_callback(self) -> None:
        self.__solution_count += 1
        for v in self.__variables:
            print(f"{v}={self.value(v)}", end=" ")
        print()

    @property
    def solution_count(self) -> int:
        return self.__solution_count
```

### C++

```c++
Model model;

int num_solutions = 0;
model.Add(NewFeasibleSolutionObserver([&](const CpSolverResponse& r) {
  LOG(INFO) << "Solution " << num_solutions;
  LOG(INFO) << "  x = " << SolutionIntegerValue(r, x);
  LOG(INFO) << "  y = " << SolutionIntegerValue(r, y);
  LOG(INFO) << "  z = " << SolutionIntegerValue(r, z);
  num_solutions++;
}));
```

### Java

```java
static class VarArraySolutionPrinter extends CpSolverSolutionCallback {
  public VarArraySolutionPrinter(IntVar[] variables) {
    variableArray = variables;
  }

  @Override
  public void onSolutionCallback() {
    System.out.printf("Solution #%d: time = %.02f s%n", solutionCount, wallTime());
    for (IntVar v : variableArray) {
      System.out.printf("  %s = %d%n", v.getName(), value(v));
    }
    solutionCount++;
  }

  public int getSolutionCount() {
    return solutionCount;
  }

  private int solutionCount;
  private final IntVar[] variableArray;
}
```

### C#

```c#
public class VarArraySolutionPrinter : CpSolverSolutionCallback
{
    public VarArraySolutionPrinter(IntVar[] variables)
    {
        variables_ = variables;
    }

    public override void OnSolutionCallback()
    {
        {
            Console.WriteLine(String.Format("Solution #{0}: time = {1:F2} s", solution_count_, WallTime()));
            foreach (IntVar v in variables_)
            {
                Console.WriteLine(String.Format("  {0} = {1}", v.ToString(), Value(v)));
            }
            solution_count_++;
        }
    }

    public int SolutionCount()
    {
        return solution_count_;
    }

    private int solution_count_;
    private IntVar[] variables_;
}
```

### Call the solver

The following code calls the solver, and passes the solution printer to it.

### Python

```python
solver = cp_model.CpSolver()
solution_printer = VarArraySolutionPrinter([x, y, z])
# Enumerate all solutions.
solver.parameters.enumerate_all_solutions = True
# Solve.
status = solver.solve(model, solution_printer)
```

### C++

```c++
SatParameters parameters;
parameters.set_enumerate_all_solutions(true);
model.Add(NewSatParameters(parameters));
const CpSolverResponse response = SolveCpModel(cp_model.Build(), &model);
```

### Java

```java
CpSolver solver = new CpSolver();
VarArraySolutionPrinter cb = new VarArraySolutionPrinter(new IntVar[] {x, y, z});
// Tell the solver to enumerate all solutions.
solver.getParameters().setEnumerateAllSolutions(true);
// And solve.
CpSolverStatus unusedStatus = solver.solve(model, cb);
```

### C#

```c#
CpSolver solver = new CpSolver();
VarArraySolutionPrinter cb = new VarArraySolutionPrinter(new IntVar[] { x, y, z });
// Search for all solutions.
solver.StringParameters = "enumerate_all_solutions:true";
// And solve.
solver.Solve(model, cb);
```

### Run the program

The complete program is shown in the [next section](https://developers.google.com/optimization/cp/cp_solver#all_solutions_program).
When you run the program, it displays all 18 feasible solutions:

```
x=1 y=0 z=0
x=2 y=0 z=0
x=2 y=1 z=0
x=2 y=1 z=1
x=2 y=1 z=2
x=2 y=0 z=2
x=2 y=0 z=1
x=1 y=0 z=1
x=0 y=1 z=1
x=0 y=1 z=2
x=0 y=2 z=2
x=1 y=2 z=2
x=1 y=2 z=1
x=1 y=2 z=0
x=0 y=2 z=0
x=0 y=1 z=0
x=0 y=2 z=1
x=1 y=0 z=2
Status = FEASIBLE
```

### Complete programs

The complete programs are shown below.

### Python

```python
from ortools.sat.python import cp_model


class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, variables: list[cp_model.IntVar]):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0

    def on_solution_callback(self) -> None:
        self.__solution_count += 1
        for v in self.__variables:
            print(f"{v}={self.value(v)}", end=" ")
        print()

    @property
    def solution_count(self) -> int:
        return self.__solution_count


def search_for_all_solutions_sample_sat():
    """Showcases calling the solver to search for all solutions."""
    # Creates the model.
    model = cp_model.CpModel()

    # Creates the variables.
    num_vals = 3
    x = model.new_int_var(0, num_vals - 1, "x")
    y = model.new_int_var(0, num_vals - 1, "y")
    z = model.new_int_var(0, num_vals - 1, "z")

    # Create the constraints.
    model.add(x != y)

    # Create a solver and solve.
    solver = cp_model.CpSolver()
    solution_printer = VarArraySolutionPrinter([x, y, z])
    # Enumerate all solutions.
    solver.parameters.enumerate_all_solutions = True
    # Solve.
    status = solver.solve(model, solution_printer)

    print(f"Status = {solver.status_name(status)}")
    print(f"Number of solutions found: {solution_printer.solution_count}")


search_for_all_solutions_sample_sat()
```

### C++

```c++
#include <stdlib.h>

#include "absl/base/log_severity.h"
#include "absl/log/globals.h"
#include "ortools/base/init_google.h"
#include "ortools/base/logging.h"
#include "ortools/sat/cp_model.h"
#include "ortools/sat/cp_model.pb.h"
#include "ortools/sat/cp_model_solver.h"
#include "ortools/sat/model.h"
#include "ortools/sat/sat_parameters.pb.h"
#include "ortools/util/sorted_interval_list.h"

namespace operations_research {
namespace sat {

void SearchAllSolutionsSampleSat() {
  CpModelBuilder cp_model;

  const Domain domain(0, 2);
  const IntVar x = cp_model.NewIntVar(domain).WithName("x");
  const IntVar y = cp_model.NewIntVar(domain).WithName("y");
  const IntVar z = cp_model.NewIntVar(domain).WithName("z");

  cp_model.AddNotEqual(x, y);

  Model model;

  int num_solutions = 0;
  model.Add(NewFeasibleSolutionObserver([&](const CpSolverResponse& r) {
    LOG(INFO) << "Solution " << num_solutions;
    LOG(INFO) << "  x = " << SolutionIntegerValue(r, x);
    LOG(INFO) << "  y = " << SolutionIntegerValue(r, y);
    LOG(INFO) << "  z = " << SolutionIntegerValue(r, z);
    num_solutions++;
  }));

  // Tell the solver to enumerate all solutions.
  SatParameters parameters;
  parameters.set_enumerate_all_solutions(true);
  model.Add(NewSatParameters(parameters));
  const CpSolverResponse response = SolveCpModel(cp_model.Build(), &model);

  LOG(INFO) << "Number of solutions found: " << num_solutions;
}

}  // namespace sat
}  // namespace operations_research

int main(int argc, char* argv[]) {
  InitGoogle(argv[0], &argc, &argv, true);
  absl::SetStderrThreshold(absl::LogSeverityAtLeast::kInfo);
  operations_research::sat::SearchAllSolutionsSampleSat();
  return EXIT_SUCCESS;
}
```

### Java

```java
package com.google.ortools.sat.samples;

import com.google.ortools.Loader;
import com.google.ortools.sat.CpModel;
import com.google.ortools.sat.CpSolver;
import com.google.ortools.sat.CpSolverSolutionCallback;
import com.google.ortools.sat.CpSolverStatus;
import com.google.ortools.sat.IntVar;

/** Code sample that solves a model and displays all solutions. */
public class SearchForAllSolutionsSampleSat {
  static class VarArraySolutionPrinter extends CpSolverSolutionCallback {
    public VarArraySolutionPrinter(IntVar[] variables) {
      variableArray = variables;
    }

    @Override
    public void onSolutionCallback() {
      System.out.printf("Solution #%d: time = %.02f s%n", solutionCount, wallTime());
      for (IntVar v : variableArray) {
        System.out.printf("  %s = %d%n", v.getName(), value(v));
      }
      solutionCount++;
    }

    public int getSolutionCount() {
      return solutionCount;
    }

    private int solutionCount;
    private final IntVar[] variableArray;
  }

  public static void main(String[] args) throws Exception {
    Loader.loadNativeLibraries();
    // Create the model.
    CpModel model = new CpModel();

    // Create the variables.
    int numVals = 3;

    IntVar x = model.newIntVar(0, numVals - 1, "x");
    IntVar y = model.newIntVar(0, numVals - 1, "y");
    IntVar z = model.newIntVar(0, numVals - 1, "z");

    // Create the constraints.
    model.addDifferent(x, y);

    // Create a solver and solve the model.
    CpSolver solver = new CpSolver();
    VarArraySolutionPrinter cb = new VarArraySolutionPrinter(new IntVar[] {x, y, z});
    // Tell the solver to enumerate all solutions.
    solver.getParameters().setEnumerateAllSolutions(true);
    // And solve.
    CpSolverStatus unusedStatus = solver.solve(model, cb);

    System.out.println(cb.getSolutionCount() + " solutions found.");
  }
}
```

### C#

```c#
using System;
using Google.OrTools.Sat;

public class VarArraySolutionPrinter : CpSolverSolutionCallback
{
    public VarArraySolutionPrinter(IntVar[] variables)
    {
        variables_ = variables;
    }

    public override void OnSolutionCallback()
    {
        {
            Console.WriteLine(String.Format("Solution #{0}: time = {1:F2} s", solution_count_, WallTime()));
            foreach (IntVar v in variables_)
            {
                Console.WriteLine(String.Format("  {0} = {1}", v.ToString(), Value(v)));
            }
            solution_count_++;
        }
    }

    public int SolutionCount()
    {
        return solution_count_;
    }

    private int solution_count_;
    private IntVar[] variables_;
}

public class SearchForAllSolutionsSampleSat
{
    static void Main()
    {
        // Creates the model.
        CpModel model = new CpModel();

        // Creates the variables.
        int num_vals = 3;

        IntVar x = model.NewIntVar(0, num_vals - 1, "x");
        IntVar y = model.NewIntVar(0, num_vals - 1, "y");
        IntVar z = model.NewIntVar(0, num_vals - 1, "z");

        // Adds a different constraint.
        model.Add(x != y);

        // Creates a solver and solves the model.
        CpSolver solver = new CpSolver();
        VarArraySolutionPrinter cb = new VarArraySolutionPrinter(new IntVar[] { x, y, z });
        // Search for all solutions.
        solver.StringParameters = "enumerate_all_solutions:true";
        // And solve.
        solver.Solve(model, cb);

        Console.WriteLine($"Number of solutions found: {cb.SolutionCount()}");
    }
}
```