import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './pages/Student/Home/Home';
import Login from './pages/Student/Login/Login';
import Query from './pages/Student/Query/Query';
import TeacherLogin from './pages/Professor/TeacherLogin/TeacherLogin';
import Absence from './pages/Student/Query/Absence/Absence';
import RollCall from './pages/Professor/RollCall/RollCall';
import Students from './pages/Professor/Studants/Students';
import Grade from './pages/Student/Query/Grade/Grade';
import Class from './pages/Student/Query/Class/Class';

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/student/home" element={<Home />} />
        <Route path="/student/query" element={<Query />} />
        <Route path="/professor/teacherLogin" element={<TeacherLogin />} />
        <Route path="/student/query/absence" element={<Absence />} />
        <Route path="/professor/rollcall" element={<RollCall />} />
        <Route path="/professor/students" element={<Students />} />
        <Route path="/student/query/grade" element={<Grade />} />
        <Route path="/student/query/class" element={<Class />} />
      </Routes>
    </BrowserRouter>
  );
};

export default App;
