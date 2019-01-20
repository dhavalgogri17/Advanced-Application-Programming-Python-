//
//  ViewController.swift
//  Lab6
//
//  Created by Dhaval Gogri on 11/10/18.
//  Copyright © 2018 Dhaval Gogri. All rights reserved.
//


//Server URL of Tornado and MongoDB

import UIKit
import CoreMotion

class ViewController: UIViewController, URLSessionDelegate, UIImagePickerControllerDelegate, UINavigationControllerDelegate {

    var SERVER_URL:String = "http://10.8.105.18:8000"

    //Variable declaration for session, queue and buffer
    var session = URLSession()
    let operationQueue = OperationQueue()
    let defaults = UserDefaults.standard
    
    
    // UI component outlets from Main.Storyboard
    @IBOutlet weak var buttonTakePicture: UIButton!
    @IBOutlet weak var imageViewRPS: UIImageView!
    @IBOutlet weak var labelPredition: UILabel!
    @IBOutlet weak var activityIndicatorView: UIView!
    @IBOutlet weak var segment: UISegmentedControl!
    
    //Variable declaration
    var dsid:Int = 1
    var isImageCaptured = false
    var isImageUploading = false
    var segmentControlOptionSelected = 0
    
    
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        if(defaults.integer(forKey: "DSID") == 0){
            self.defaults.set(1, forKey: "DSID")
            self.dsid = 1
        }
        else{
            self.dsid = defaults.integer(forKey: "DSID")
        }
        
        
        if(defaults.string(forKey: "IP_ADDRESS") == ""){
            self.defaults.set("http://10.8.105.18:8000", forKey: "IP_ADDRESS")
            self.SERVER_URL = self.defaults.string(forKey: "IP_ADDRESS")!
        }
        else{
            self.SERVER_URL = self.defaults.string(forKey: "IP_ADDRESS")!
        }
        
        
        //Setting up session, Delegate, setting default values
        let sessionConfig = URLSessionConfiguration.ephemeral
        sessionConfig.timeoutIntervalForRequest = 30.0
        sessionConfig.timeoutIntervalForResource = 30.0
        sessionConfig.httpMaximumConnectionsPerHost = 1
        
        self.session = URLSession(configuration: sessionConfig,
                                  delegate: self,
                                  delegateQueue:self.operationQueue)
        
        
        
    }
    
    
    

    
    func getPrediction(_ array:String){
        //Show activity indicator when making network calls
        self.activityIndicatorView.alpha = 1
        
        //Creating a base and post URL
        let baseURL = "\(SERVER_URL)/PredictOne"
        let postUrl = URL(string: "\(baseURL)")
        
        // create a custom HTTP POST request
        var request = URLRequest(url: postUrl!)
        
        // data to send in body of post request (send arguments as json)
        //
        let jsonUpload:NSDictionary = ["feature":array, "dsid":self.dsid]
        
        let requestBody:Data? = self.convertDictionaryToData(with:jsonUpload)
        
        request.httpMethod = "POST"
        request.httpBody = requestBody
        
        let postTask : URLSessionDataTask = self.session.dataTask(with: request,
                                                                  completionHandler:{(data, response, error) in
                                                                    DispatchQueue.main.async {
                                                                        
                                                                        if(error != nil){
                                                                            if let res = response{
                                                                                print("Response:\n",res)
                                                                            }
                                                                            self.showAlertBox("Error")
                                                                            self.imageViewRPS.image = UIImage(named:"fruit_placeholder_2")!
                                                                            self.isImageCaptured = false
                                                                        }
                                                                        else{
                                                                            //Get data from server and store it in dictionary
                                                                            let jsonDictionary = self.convertDataToDictionary(with: data)
                                                                            //If there is some data present, it means success
                                                                            if(jsonDictionary.count > 0){
                                                                                NSLog("Data\nData\nData")
                                                                                NSLog("\(jsonDictionary)")
                                                                                NSLog("Data\nData\nData")
                                                                                // Get the prediction data from the dictionary and convert it
                                                                                // into a utf-8 string format
                                                                                let prediction = (jsonDictionary["prediction"]! as! String).utf8
                                                                                print(prediction)
                                                                                //show the prediction to the user
                                                                                self.labelPredition.text = "Prediction is : \(prediction) using CNN"

                                                                            }
                                                                            else{
                                                                                self.showAlertBox("Error in getting prediction")
                                                                            }
                                                                        }
                                                                        self.activityIndicatorView.alpha = 0
                                                                        
                                                                    }
                                                                    
        })
        
        postTask.resume() // start the task
    }
    
    
    

    
    //MARK: JSON Conversion Functions
    func convertDictionaryToData(with jsonUpload:NSDictionary) -> Data?{
        do { // try to make JSON and deal with errors using do/catch block
            let requestBody = try JSONSerialization.data(withJSONObject: jsonUpload, options:JSONSerialization.WritingOptions.prettyPrinted)
            return requestBody
        } catch {
            print("json error: \(error.localizedDescription)")
            return nil
        }
    }
    
    //Converting the data we get from the server to an NSDictionary
    func convertDataToDictionary(with data:Data?)->NSDictionary{
        do { // try to parse JSON and deal with errors using do/catch block
            let jsonDictionary: NSDictionary =
                try JSONSerialization.jsonObject(with: data!,
                                                 options: JSONSerialization.ReadingOptions.mutableContainers) as! NSDictionary
            
            return jsonDictionary
            
        } catch {
            print("json error: \(error.localizedDescription)")
            return NSDictionary() // just return empty
        }
    }
    
    // Taking image from camera button
    @IBAction func takePictureFromCamera(_ sender: UIButton) {
        //Initialize an ImagePickerController which would help in selecting an image using a camera
        let vc = UIImagePickerController()
        // apply delegate, source type and editing
        vc.delegate = self
        //vc.sourceType = .camera
        vc.sourceType = .camera
        vc.allowsEditing = true
        present(vc, animated: true)
    }
    

    
    //Take picture from the camera
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey : Any]) {
        picker.dismiss(animated: true)
        // If image not present, error and return
        guard let image = info[.editedImage] as? UIImage else {
            print("No image found")
            return
        }
        //If image image present. Apply that into the image view
        isImageCaptured = true;
        self.imageViewRPS.image = image
        //If the prediction tab is ON, then send the image to the server for prediction
        if(isImageCaptured && !isImageUploading){
            //Convert the image data into a base64 string before sending it to the server
            let imageData:NSData = self.imageViewRPS.image!.jpegData(compressionQuality: 100)! as NSData
            let strBase64 = imageData.base64EncodedString(options: .lineLength64Characters)
            //Get prediction from the server
            self.getPrediction(strBase64)
        }
    }
    
    
    
    
    
    
    func imagePickerControllerDidCancel(_ picker: UIImagePickerController) {
        picker.dismiss(animated: true)
    }
    
    func numberOfComponents(in pickerView: UIPickerView) -> Int {
        return 1
    }
    
    
    
    
    
    //Show alert messages wherever necessary
    func showAlertBox(_ message: String?) {
        let alert = UIAlertController(title: "INFORMATION", message: message, preferredStyle: .alert)
        
        // Only when the user presses the 'GOT IT!' button, the game scene is created
        let okButton = UIAlertAction(title: "GOT IT!", style: .default, handler: { action in
            
            alert.dismiss(animated: true)
        })
        
        alert.addAction(okButton)
        present(alert, animated: true)
    }
    
    
    
    
    
}





