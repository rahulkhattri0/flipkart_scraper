import streamlit as st
import requests
from bs4 import BeautifulSoup
def get_url(brand):
        domain='https://www.flipkart.com/search?q='
        keyword=brand
        url=domain+keyword.replace(' ','%20')
        return url
def fetchdata(url):
    try:
        data=requests.get(url)
        return data
    except Exception as e:
        print("some error")
        print(e)
def parseData(text):
    try:
        soup=BeautifulSoup(text,features='html.parser')
        return soup
    except Exception as e:
        print('error while parsing')
        print(e)
def products(brand):
    try:
        soup=None 
        try:
            data=fetchdata(get_url(brand))
            if data.status_code==200:
                soup=parseData(data.text)
                    
            else:
                print('no data')
        except Exception as e:
                print(e)
        products=soup.find_all('div',attrs={'class':"_1AtVbE col-12-12"})
        for prod in products[3:-4]:
            
            print(prod.find_all('div', {'class' : 'CXW8mj'})[0])
            rr = prod.find('span', {'class' : '_2_R_DZ'})

            rating_text = rr.find('span').find_all('span')[0].text.split()[0].replace(',', '')
            

            review_text = rr.find('span').find_all('span')[-1].text.split()[0].replace(',', '')
            
            st.image('https://rukminim1.flixcart.com/image/312/312/kfzq8i80/television/e/j/y/oneplus-32h0a00-original-imafwb6wmqxh2ung.jpeg?q=70',output_format="auto")
            cols = st.beta_columns(4)
            cols[0].write(prod.find('div', {'class' : '_4rR01T'}).text)
            cols[1].write(prod.find('div', {'class' : '_30jeq3'}).text)
            cols[2].write(rating_text+" ratings")
            cols[3].write(review_text+" reviews")
    except Exception as e:
        st.write(e)
st.title("flipkart scraper")
st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAASwAAACoCAMAAABt9SM9AAABXFBMVEX///8AfNj/5AD/0QD/2wD/zQD/1wD/3wD+6AD/2QD/zwD/3QD/5gAAdNb/1AAAedcAcNUAddb/+uz96aP67Xf/4Y3/nAAAdeGcwOvD2PIAbtUAXrxcnOD6zYAwiNv/yQD64oH/uAD/sAD/wADP4PXZ5vdCkN3/5Z7/ugDy9/yPuOiDseZSl9+lxezV5Pb/sgD/qQBpo+Lk7vm70/H00SP9/fh3quQXgdn+3Jzz+P2ItOevy+7BpAIAbun63oH61oHYugEsg85wl7D97LH98L7922D99tj+8MrhvAbvxgfNrgb96Tj962X98JT9+uX64Wv+7Fz/6Ej/983/7oPp37rbyonXwmL+8aX/+cD/8J/w1yXZyUXJwFW9uWLAu16UoX9Nf6OlsYMAaru7vHWJm4VpipeKpp5Xkb1/oKYAacWurG5BicZ9ko08d6jixzwmcbDcxE+mpnSUmYDEy8U0e8lDAAAN5UlEQVR4nO2cj1vbNhrH7SQQIHFsZ7vlx3Kh7ZIMSKBHSMjSpB1lPVZS2nHXu239yVi7Qn8c1+7+/+c5ydIrS7LsmBJIn6Lvs7WJJdnWR6/eV6/sxjC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tM5f+R+++EjdmfatX7Tu/H1mcUbWgkqBWqjhlZ1p3/8F6s7CYoBQMkLAjbFbTD6Ydh8uTN8tLYqsokjxvJhxXf1x2n24MH13/fpVHtXC3d1cJKrduxQXQXX9+rXLMxExrBywQhiGw+EutR+EAoQreEdzW8PhKOcbVxLBukSWdW1xLjPDJuDucDTcyhFO3wjCxBaSudFoNGRzcWYmm/3mMsFKzc1lOGeFLWvGA7W0tHSVaWmJ8Fq461kW4JpJzM0tXJpp+OvcHIHFvPfd3UUMCgG6jqYYEfpEgS0uYp/FHD2GNXfvctDq7mUpLADgGdUSBnXt2t94YWQeL2RePi0P1lz2/rQ7cgH6p4cKw4LeI1SElAfoK04EGObF4yKw5rL3Pvu11h5lBbAWPKPyQH2lFgZ2/SqejTMCrLns525c3Z+uSLp169b3RH8NESlF9W7Jba9Muzvnq+7elxPUw2l353yVh1k4GU27O+ervKrL2cS9cVT2ExoWYZV7YOxFs9oxvpi/hLAU0zC7YBj3I1ll80Y+qTo+7e6cr5Q+K4VgRfqy7E53J3MJYSWyCuWNX1WHmRJ4Las+/jlLDWsn5DjoXrf7SFlwlltZrtf7k+rW+SifCAgZyH2j+49gAauAyo19VC1YIJy7WFVqxStc8T632lC51nMcp9yKh+sGaXzRbJWwvGkWDiuReGB0E2Nh1cu2UuUaKlwjhW6LVi6VbRPJrcS56RJtvD5pGmOkgIX1C1rah7N6aHQfqUv4U2+4plJWCRWukkK7QStDoRPnpou0cSyyE1QIrETeMO6FwuoaRkgJf+qVEFgOnnpN2t9NUnfNOg2sdc8KTXdlkiRqpVKpHl0lDNa+kQ8rSuS73SsxYFXsEFi4sEX7u0rqDgCsHadfVdLY2vgYKCHqOZZllTcj64QSQTlxfl9ZsmMY/0rHgNVTszJNXGhzUxJpg1qWG323VA6lPsYQTqOSE8OwQ2Gl/40m2y/B41+iNj/eDTr3ICzaJdO1BJWxMfWhvzQa9svErtw4Aa4NjT8SjEqb3ujZ1chK+TAbyd792TC6CBdXIZ3+8gE+NgpjxcOCLrkr2BuAajXPHOpyf0sWmgblRjtwgwqVwMF9DJUQEUu3o+NrKKxEdrT1Kyo3dh7tIUrpdGL/4R1EyniwN/Lb0IW7ChbMLEs1WWik5EeyXqotx+sYRNLW+KpxRQfPLUbWyqdDlRht7e9g6+piZuRvtHJPjzoEHiL1+MnTZ8+eP0kkoA13ZhrfTUc1s2ikHDOSIdqkweHGxzRWi97smJARAQvRGmXu/bLjQfL+e3BnLzE/9Fhls08OfntddhwLLbydw2wQFo3vpqu6LI2U/ki26/V2GyYh+tQGxO3V9UajssKbZ4M2Hhhc/bY4g/ul4mal0Wi01pvFDT6N4mv2B038ud9uwyk30H1EwMpE0doabqG/9h/ef/To0cN9dCC1NZxHrLKPD34vu/7SoPAiEYBF4ztbdgqikZKNZKWMmZeJrRTxGJTX8Mdaw3G9xbrD5TbUZK01+r3pNXZ6/uk3Wo7l0oTBddF4mhVKFidVDpn8/U3HdZHd11Bz6IqLi0MdZySsdGJ+NNzqZIiTT6d2Rx68RPrl1+KC076dDcCiLtxWLgak4N8u0/77hW4TdafCemHaNni0ZWhMD/ShcQlQmVZgiWeXvXEhKwQHYx44uA+IzLpUOXytGw0LgemMhsPhCL/cgLSVwmb19PfA2rzwWIbFgqHKZ8rBv0aDQc+HgWCtuXw37J5UGeb3KjhHahEVx1SI3AfxTRhWxYI7kNeDbqjjGgcLW9eWB2q01Ul73url18FbKbyQYUF8Z+PNq8TD8ftLkj0CA604yuI1LDriA3VaCd976iyL3AeJDQhrww/HMtuPnYbAK0H+9z7/8Vp1K68SEix5vAXJmXCTT/YIDLsR6DSZpMYN2rgpXYiMSjUsyfLugzhyZxlOjpxEXxoTsxzGKh4sTlklK9M+kmHR+K5eZsvBnwUjHgb503IYNBoOKmJaSY2UztJ1lmRajtmzHea9yH3QUkYUn2S9bLEr4MgSvtY6JazsSyUr034rw6L9R9bD1KqsiYUs+EN8q3MwSBdbtbafZJNYAR2rETowKJ5hlWBOOfRadTouZPm7LE05u4yvuAxe0KpxaxYVrFTmFEo/D/orLz4XttNeBf/EllBO5YiFEPxZfOtzMLwDHk3wcHS9L6SVGxB0KzxI02FOepVf/tYs7uS25VbI1IULjEs2TwUrnZHsyrYKBbPXu310SFj5sOQxFO5GhOPvZtk8DFxOjIdZqddcSCshrJqWd6oB9JqtV2HjjHeHtE6rJgONTqMRrPlUfKXfibAs8+Ak7SXYaVqDnVcYQx+uWAibVwM+2aszWMDKz5zwF5pzesGvbwJGYkl0FcAvhFv83tcNBsu2uSjdjJl8nQZWpiNOwsJxOp0Rq7DzDlQBHFJfAY7fB7fJwUAAVuFkwjSBtBLFsYENKRXpZl2x0WXzh5g7dIW8oiUnXxOAJRlW4WUiUEUeLFFuUyiEryy+DTgY/A57jYcFHr3aY3ES5s9KcDr1heUvuxFx954eHbvzegpYmZRgWGi1EKwjD5ZpO5yqfXEkwXTgZms8DG4fUIBVDYyBbdKqjaCFrAl7XxANxHy1H3fn9RSw0i9Ew3qcCdZh5wVWSjcgwPH7QJK9qkTS8Gdmj6vMa1k8D8uwjRB3aIm3E9iJnASsP/jFsbudVtSB08JgqZNSaU9Z7INUiMUv+NuByGGxnR0pyGIJy18+NnBiz+wmCUuYhYXnCsNisFj/VW5AHmChD6oNdn73qxSAxWxwLbhcYuk87w7ljZAVbiyiYc3Ox1TqiTgLU6pKcFoYLKUbADjgh4t8H0pSIRbArfmVTduFPQlWVbG2hLxGcIdy1KtIydcEYGXe8LDst+koWBDSYu0pr/Neqhhc88AyxLNESF9axWJDWBaoYG3CBKPukJ5H2gjp8dYXCSs3G1OZd4LLOk6pKsFp2Yaa6pryAMMzU24TRXB2MD6e5TX8RWYN5lhTggXmvMqCAdn7UrhD7jCLN5OA9R8elnUYCYuOofoBTJVfVsl9aPArbk9gHqScD/OwbUedXx12BekoDBgr6g7VKWBbylQnAUtcZRWezkfBgjFXugEopI5ZdOmydRhFIVUWIh5sZVGyfj4qNDQld2hym/X84TNOQ8EdnYiwSGEIrHbU9aG/4JgFlw4dBr+y1mLZj2dYQloJCxRYC4Dp2622UWtxYVN0h1LUY/mVvVqrRT4RV8Kax+uJTCYz2+H0RkyiSdlsSgmL7Smr3ADLlG2ngv2uehPFcnqtSsNlTywsMrfEB6xsM6stfMV5g/DMQnSHkrkzWKZrOZHvDwRgzafmOyfP3xy8++2/r7/m9fp3ARY9+i6jgsW2CVTPmP1tBdNqGpJL5xNw2/Y7DJkvbEATn14Tp3twq8PucTADzxuNYKvI/DAA6+mrt+7Nm4VCQXi0EirJd9Gzwp6y8gErt+nt+RLBpSsTcHQiWEtJHQYXTzd7pA1426JPTwV3KJu7sAkfGRIRrBwS9weag7Mnzw6Oj8xCDFjW4XzOF8BqRD1gZUk2tSbBpbeUQ2QxNwMunfapKLr4uvDwwe21CU3RHQbMnd/HtqJeTQnA8j54vj1zEoOW82Geaw+w/GcnKrVZl6yBP7DkoYqKlctNHKgMD1ilpdYqZ7XOOpyPukN1Go0jjn/V8Ec7GFYypxKGleuEvo7mq/B8lm9Hz3qjTF7FClm5rLme+7UtC/e5hd+5s5wK33mTuiv84L7H7T9AZWayTXolmD0bluc+ULNGjd1JmYRW02tbbhqy2j0HXw9drBz55qUa1tPDbfPmzZshL4UKsDo5BSyjXsMKf4VoUOnZvQqlQN7fIu0orOpmw3Qcx26sr0rzgrzl5X+vbZRqpQ3uSquVnms22Jsk+OTtkLbcWTertl3dHES/9BRiWci0Ou9fbI/18fZt3mUlc5HXiqFBMDP8hIRgJXEvOWb+gvT9WKdVOMix9skJwKI59iRfvZqg8uyf3HdOTn7++cWbgz9fHW8fHb2t2mj5MI6V2xN/heXMsCrqpdAnIgrr5P2zF28ODw9evjo+3sas3t7u4YeCTOJyz6ZHjzoThgXvbaneJpm+wLIkj0XlodjdTe7mPgibWbdz6Fiyk5yVf9DnrLcD0T3Wi7gXrnyMX39CmhU2s+ztsN9AOuPdnMdL2xNUXFjiZtbBOcGCBHzcc/QpKSasnLg/8+ycYCn2lD8lxYR1Ij6s6ITVO+PdhDxR+FSUV/8KoqTkMwGWmwureMa7KZZdrPIE/1HOJBUT1p985mMfnRcsY7CCVBz75GBKygd/cFOhpPgw+jgZUu/MsD5txYOVE3ZJrQ+KHyslmnZ3zllxYC3sisHwfRisn6bdm3PWtzFoLbwXg2FYvcXP/tfGfhpPa+GD4/qyeiEua/ES/Mjyzrd/GaNb/yvyKn2r1A/dafdES0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLi+j/Fob7MX/ZUG8AAAAASUVORK5CYII=')
brand=st.text_input("enter brand name")
st.table(products(brand))
