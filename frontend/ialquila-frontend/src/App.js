import './App.css';
import Nav from './components/Nav';
import PrincipalContainer from './components/PrincipalContainer';
import Detail from './components/Detail';
import Landing from './components/Landing';
import { BrowserRouter, Route, Routes } from 'react-router-dom';


function App() {

  return (
    <BrowserRouter>
      <Nav />
      <Routes>
        <Route path='/' element={<Landing/>}/>
        <Route path='/todo' element={<PrincipalContainer/>} />
        <Route path='/departamentos' element={<PrincipalContainer/>}/>
        <Route path='/casas' element={<PrincipalContainer/>}/>
        <Route path='/informacion' />
      </Routes>
    </BrowserRouter>  
  );
}

export default App;
