import { BrowserRouter, Route, Routes } from 'react-router-dom';
import './App.css';
import Sidebar from './components/sidebar/Sidebar';
import ProtectedRoute from './components/react_router/ProtectedRoute';
import LoginContextProvider from './contexts/LoginContextProvider';
import LoginPage from './pages/auth/LoginPage';
import HomePage from './pages/home/HomePage';
import LoadingBar from 'react-top-loading-bar';
import { loadingRef } from './refs/LoadingRef';
import SettingPage from './pages/settings/SettingPage';
import NewPOPage from './pages/new_po/NewPOPage';
import PurchaseOrderPage from './pages/purchase_orders/PurchaseOrderPage';
// import InventoryPage from './pages/inventory/InventoryPage';
import NotFoundPage from './pages/error/NotFoundPage';
import POMonthYearProvider from './contexts/POMonthYearProvider';
import ProfileContextProvider from './contexts/ProfileContextProvider';
import PODataProvider from './contexts/PODataProvider';
import ProductDataProvider from './contexts/ProductDataProvider';
import BaseRedirectPage from './pages/home/BaseRedirectPage';
import SignUpPage from './pages/auth/SignUpPage';
import CreateShopPage from './pages/auth/CreateShopPage';

function App() {
  return (
    <BrowserRouter>
      <PODataProvider>
        <POMonthYearProvider>
          <ProfileContextProvider>
            <ProductDataProvider>
              <LoginContextProvider>
                <LoadingBar ref={loadingRef} color='#0BC5EA' />

                <Routes>
                  <Route path='/login' element={<LoginPage />} />
                  <Route path='/create-account' element={<SignUpPage />} />
                  <Route path='/create-shop' element={<CreateShopPage />} />

                  <Route path='/' element={<ProtectedRoute />} >
                    <Route path='/' element={<BaseRedirectPage />} />
                  </Route>

                  <Route path='/' element={<ProtectedRoute />}>
                    <Route path='/home' element={
                      <Sidebar>
                        <HomePage />
                      </Sidebar>
                    } />
                  </Route>

                  {/* <Route path='/' element={<ProtectedRoute />}>
                    <Route path='/inventory' element={
                      <Sidebar>
                        <InventoryPage />
                      </Sidebar>
                    } />
                  </Route> */}

                  <Route path='/' element={<ProtectedRoute />}>
                    <Route path='/purchase-order' element={
                      <Sidebar>
                        <PurchaseOrderPage />
                      </Sidebar>
                    } />
                  </Route>

                  <Route path='/' element={<ProtectedRoute />}>
                    <Route path='/new-purchase' element={
                      <Sidebar>
                        <NewPOPage />
                      </Sidebar>
                    } />
                  </Route>

                  <Route path='/' element={<ProtectedRoute />}>
                    <Route path='/settings' element={
                      <Sidebar>
                        <SettingPage />
                      </Sidebar>
                    } />
                  </Route>

                  <Route path='*' element={<NotFoundPage />} />
                </Routes>
              </LoginContextProvider>
            </ProductDataProvider>
          </ProfileContextProvider>
        </POMonthYearProvider>
      </PODataProvider>
    </BrowserRouter >
  );
}

export default App;
