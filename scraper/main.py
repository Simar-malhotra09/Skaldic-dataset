from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from concurrent.futures import ThreadPoolExecutor


base_url = "https://skaldic.org/m.php?p=text&i="
output_file = "output_all.txt"

# Configure the Selenium webdriver (make sure you have the appropriate webdriver installed, e.g., chromedriver)
driver = webdriver.Chrome()

with open(output_file, "w", encoding="utf-8") as output:
    for x in range(1000,  3000#2000):
        url = base_url + str(x)

        try:
            driver.get(url)
            
            # Wait for the content to be present on the page
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ui-grid-b.ui-responsive")))

            parent_element = driver.find_element(By.CLASS_NAME, "ui-grid-b.ui-responsive")

            # Get the content from the specific element with class "ui-block-b" within the parent
            content_element = parent_element.find_element(By.CLASS_NAME, "ui-block-b")
            content = content_element.text
            
            # Write the content to the file
            output.write(content)
            output.write('\n')
            
            #print(f"Page for x={x} downloaded successfully.")

        except Exception as e:
            continue

# Close the webdriver
driver.quit()

# Print a message when the loop is finished
print(f"All pages downloaded and saved to {output_file}.")
