
class Worker:

    def __init__(self, unique_identifier: str, name, job_title):
        self.unique_identifier = unique_identifier
        self.name = name
        self.job_title = job_title

    def get_unique_identifier(self):
        return self.unique_identifier
    def get_name(self):
        return self.name
    def get_job_title(self):
        return self.job_title


class Employee(Worker):

    def __init__(self, unique_identifier: str, name, job_title, monthly_salary: float):
        super().__init__(unique_identifier, name, job_title)
        self.monthly_salary = monthly_salary
        self.last_promotion = 0

    def promote(self):
        if self.last_promotion < 2000:
            self.last_promotion += 500 
        self.monthly_salary += self.last_promotion
    
    def get_monthly_salary(self):
        return self.monthly_salary
    

class Contractor(Worker):

    def __init__(self, unique_identifier: str, name, job_title, hourly_wage: float):
        super().__init__(unique_identifier, name, job_title)
        self.hourly_wage = hourly_wage
        self.hours_worked_this_month = 0
    
    def work_hours(self, hours):
        self.hours_worked_this_month += hours

    def reset_hours_worked(self):
        self.hours_worked_this_month = 0
    
    def get_monthly_salary(self):
        return self.hours_worked_this_month * self.hourly_wage
    

class Worker_tracker:

    def __init__(self, intial_workers: list[Worker]):
        self.all_workers = intial_workers

    def find_worker_by_unique_identifier(self, unique_identifier: str) -> Worker:
        for worker in self.all_workers:
            if worker.get_unique_identifier() == unique_identifier:
                return worker 
        raise ValueError(f"No worker with unique identifier {unique_identifier} was found in self.all_workers")
    
    def promote_worker(self, unique_identifier: str):
        worker = self.find_worker_by_unique_identifier(unique_identifier)
        if isinstance(worker, Employee):
            worker.promote()
        else:
            raise ValueError(f"Worker {unique_identifier} is a Contractor and so cannot be promoted")
        
    def add_worker(self, worker: Worker):
        self.all_workers.append(worker)
    
    def remove_worker(self, unique_identifier: str):
        worker = self.find_worker_by_unique_identifier(unique_identifier)
        self.all_workers.remove(worker)

    def calc_monthly_expenses(self):
        num_employees, employee_cost = 0, 0
        num_contractors, contractor_cost = 0, 0
        for worker in self.all_workers:
            if isinstance(worker, Employee):
                employee_cost += worker.get_monthly_salary()
                num_employees += 1
            else:
                contractor_cost += worker.get_monthly_salary()
                num_contractors += 1
        out = f"\n{num_employees} employees, costing £{employee_cost} last month"
        out += f"\n{num_contractors} contractors, costing £{contractor_cost} last month"
        out += f"\nTotal {num_employees + num_contractors} workers, costing £{employee_cost + contractor_cost} last month"
        return out

    def finish_month(self):
        print(self.calc_monthly_expenses())
        for worker in self.all_workers:
            if isinstance(worker, Contractor):
                worker.reset_hours_worked()


def main():
    john = Employee('a', 'John', 'Plumber', 2000)
    lisa = Employee('b', 'Lisa', 'Finance', 4000)
    dave = Contractor('c', 'Dave', 'Software Engineer', 20)
    aaron= Contractor('d', 'Aaron', 'Software Engineer', 17)
    mike = Contractor('e', 'Mike', 'Software Engineer', 17)

    worker_tracker = Worker_tracker([john, lisa, dave, aaron])

    dave.work_hours(120)
    aaron.work_hours(100)
    john.promote()
    worker_tracker.finish_month()
    worker_tracker.remove_worker('c')

    aaron.work_hours(120)
    john.promote()
    worker_tracker.finish_month()

    worker_tracker.add_worker(mike)
    mike.work_hours(95)
    aaron.work_hours(125)
    john.promote()
    worker_tracker.finish_month()

main()



    
