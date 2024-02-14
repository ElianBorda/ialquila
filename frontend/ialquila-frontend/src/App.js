import './App.css';
import Nav from './components/Nav';
import PrincipalContainer from './components/PrincipalContainer';
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
        <Route path='/*' element={<PrincipalContainer />}/>
      </Routes>
    </BrowserRouter>  
  );
}

export default App;
